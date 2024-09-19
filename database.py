import sqlite3

def init_db():
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS leave_requests
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  employee_id TEXT,
                  start_date TEXT,
                  end_date TEXT,
                  reason TEXT,
                  status TEXT)''')
    conn.commit()
    conn.close()

def get_employee_data(employee_id):
    # Fetch employee data from the database
    # Return a string with relevant employee information
    pass

def get_team_workload(employee_id, start_date, end_date):
    # Fetch team workload data for the given period
    # Return a string summarizing the team's workload
    pass

def get_employee_leave_history(employee_id):
    # Fetch the employee's leave history
    # Return a string summarizing past leave patterns
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("SELECT start_date, end_date, status FROM leave_requests WHERE employee_id=? ORDER BY start_date DESC", (employee_id,))
    leave_history = c.fetchall()
    conn.close()

    if not leave_history:
        return "No leave history found for this employee."

    history_summary = []
    for start_date, end_date, status in leave_history:
        history_summary.append(f"From {start_date} to {end_date}: {status}")

    return "\n".join(history_summary)

def get_project_deadlines(employee_id, start_date, end_date):
    # Fetch upcoming project deadlines for the employee
    # Return a string listing relevant project deadlines
    pass

def add_leave_request(employee_id, start_date, end_date, reason):
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("INSERT INTO leave_requests (employee_id, start_date, end_date, reason, status) VALUES (?, ?, ?, ?, ?)",
              (employee_id, start_date, end_date, reason, 'Pending'))
    conn.commit()
    conn.close()

def get_pending_requests():
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leave_requests WHERE status='Pending'")
    requests = c.fetchall()
    conn.close()
    return requests

def get_request_by_id(request_id):
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leave_requests WHERE id=?", (request_id,))
    request = c.fetchone()
    conn.close()
    return request

def get_all_requests():
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("SELECT * FROM leave_requests")
    requests = c.fetchall()
    conn.close()
    return requests

def update_request_status(request_id, status):
    conn = sqlite3.connect('leave_requests.db')
    c = conn.cursor()
    c.execute("UPDATE leave_requests SET status=? WHERE id=?", (status, request_id))
    conn.commit()
    conn.close()