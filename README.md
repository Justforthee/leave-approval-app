# Leave Approval System

This project is a simple Leave Approval System built with Python and Flask, demonstrating the potential of AI-enhanced decision support in HR processes. It allows employees to request leave and managers to approve or reject these requests, while leveraging OpenAI's GPT model to generate intelligent insights for each application. This application serves as a basic proof of concept, showcasing how AI can be integrated into traditional HR systems to improve decision-making.

## Technologies Used

This project utilizes several technologies to create a robust and efficient Leave Approval System:

1. **Python**: The core programming language used for backend development.
2. **Flask**: A lightweight WSGI web application framework in Python, used for routing and handling HTTP requests.
3. **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine, used for storing and managing leave request data.
4. **HTML/CSS**: Used for structuring and styling the web pages.
5. **JavaScript**: Used for client-side interactions and dynamic content updates.
6. **OpenAI GPT**: Integrated to generate intelligent insights for leave requests.

## OpenAI Integration

The Leave Approval System leverages OpenAI's GPT model to provide intelligent insights for leave requests. Here's how it's implemented:

1. **API Integration**: The system uses the OpenAI API to send requests and receive responses from the GPT model.

2. **Insight Generation**: When a manager requests insights for a leave application, the system gathers relevant data (employee history, team workload, project deadlines) and formats it into a prompt for the GPT model.

3. **Natural Language Processing**: The GPT model processes the prompt and generates human-like text that analyzes the leave request, considering factors like the employee's leave history, current team workload, and upcoming project deadlines.

4. **Decision Support**: The generated insights help managers make informed decisions about leave approvals by providing a comprehensive analysis of the situation.

5. **Dynamic Responses**: The AI-generated insights are unique for each request, taking into account the specific context and data related to that leave application.

By incorporating OpenAI's GPT, the Leave Approval System provides managers with intelligent, context-aware insights, enhancing the decision-making process for leave approvals.



## Features

- Employee leave request submission
- Manager dashboard for reviewing and managing leave requests
- Insights generation for leave requests, including:
  - Employee leave history
  - Team workload during the requested leave period
  - Upcoming project deadlines
- SQLite database for storing leave request data

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/leave-approval-system.git
   cd leave-approval-system
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. Initialize the database:
   ```
   python
   >>> from database import init_db
   >>> init_db()
   >>> exit()
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:5000`


## Project Structure

- `app.py`: Main Flask application
- `database.py`: Database operations and initialization
- `templates/`: HTML templates for the web interface
- `static/`: CSS stylesheets

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
