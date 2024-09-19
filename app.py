from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_leave_request, get_pending_requests, get_all_requests, get_request_by_id, update_request_status, get_employee_data, get_team_workload, get_employee_leave_history, get_project_deadlines
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_leave', methods=['GET', 'POST'])
def request_leave():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        reason = request.form['reason']
        add_leave_request(employee_id, start_date, end_date, reason)
        return redirect(url_for('index'))
    return render_template('request_leave.html')

@app.route('/manager_dashboard')
def manager_dashboard():
    #pending_requests = get_pending_requests()
    all_requests = get_all_requests()
    return render_template('manager_dashboard.html', requests=all_requests)

@app.route('/approve_request/<int:request_id>')
def approve_request(request_id):
    update_request_status(request_id, 'Approved')
    return redirect(url_for('manager_dashboard'))

@app.route('/reject_request/<int:request_id>')
def reject_request(request_id):
    update_request_status(request_id, 'Rejected')
    return redirect(url_for('manager_dashboard'))

def generate_insights(employee_id, start_date, end_date):
# Fetch employee data
    employee_data = get_employee_data(employee_id)
    
    # Fetch team workload
    team_workload = get_team_workload(employee_id, start_date, end_date)
    
    # Fetch employee's leave history
    leave_history = get_employee_leave_history(employee_id)
    
    # Fetch upcoming project deadlines
    project_deadlines = get_project_deadlines(employee_id, start_date, end_date)
    
    prompt = f"""Generate insights for a leave request from employee {employee_id} from {start_date} to {end_date}.

                Employee Data:
                {employee_data}

                Team Workload:
                {team_workload}

                Employee's Leave History:
                {leave_history}

                Upcoming Project Deadlines:
                {project_deadlines}

                Consider the above information and provide a detailed analysis on the following:
                1. Impact on team workload
                2. Employee's leave pattern and fairness
                3. Potential conflicts with project deadlines
                4. Recommendation for approval or rejection with justification
        """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant that generates insights for leave requests. Provide a concise analysis and decision recommendation based on the information provided."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    return response.choices[0].message.content.strip()

@app.route('/get_insights/<int:request_id>')
def get_insights(request_id):
    # Fetch request details from database
    request = get_request_by_id(request_id)
    if request:
        employee_id = request[1]
        start_date = request[2]
        end_date = request[3]
    else:
        return "Request not found", 404
    insights = generate_insights(employee_id, start_date, end_date)
    return insights

if __name__ == '__main__':
    init_db()
    app.run(debug=True)