# AI Agent & Automation System

## Project Overview

The AI Agent & Automation System is an intelligent assistant that understands natural language instructions, creates task plans, and automatically executes tasks using different tools.

The application uses a Large Language Model (LLM) to understand user instructions and decide which tools are required to complete the requested tasks.

It also provides a Streamlit web interface to interact with the AI agent and view previous conversations.

## Features

- Natural language instruction processing
- AI-based task planning
- Automatic tool selection and execution
- Calculator for mathematical operations
- Date and time information
- Real-time weather information
- Text file creation and reading
- Conversation history storage using JSON
- Error handling
- Tool usage analytics
- Interactive Streamlit dashboard

## Technologies Used

- Python
- Groq API
- OpenAI GPT-OSS model through Groq
- Streamlit
- WeatherAPI
- SQLite (not used)
- JSON
- Python Requests
- python-dotenv

## Project Structure

```text
AI-Agent-Automation-System/
│
├── app.py
├── agent.py
├── planner.py
├── llm.py
│
├── tools/
│   ├── calculator.py
│   ├── datetime_tool.py
│   ├── weather.py
│   └── file_tool.py
│
├── memory/
│   └── history.py
│
├── utils/
│
├── data/
│   ├── history.json
│   └── generated_files/
│
├── screenshots/
│
├── test_agent.py
├── test_planner.py
├── test_calculator.py
├── test_datetime.py
├── test_weather.py
├── test_file_tool.py
├── test_history.py
│
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd AI-Agent-Automation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API keys

Create a `.env` file in the project root.

Add your own API keys:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
```

Never upload your actual API keys to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## Available Tools

### 1. Calculator

Performs mathematical calculations such as addition, subtraction, multiplication, and division.

### 2. Date and Time

Provides the current date, time, and day.

### 3. Weather

Retrieves current weather information for a specified city using WeatherAPI.

### 4. File Operations

Creates and reads text files in the generated_files directory.

## Conversation Memory

The application stores user instructions, timestamps, and execution results in a JSON file.

This allows users to view their previous conversations through the dashboard.

## Example Instructions

```text
Calculate 2500 + 3500

Tell me today's date

Get weather in Hyderabad

Create a file named notes with content Hello World

Tell me the weather in an invalid city
```

## Application Interface

The Streamlit dashboard includes:

- Project dashboard
- Tool usage analytics
- AI Agent instruction section
- Agent execution results
- Conversation history

## Future Enhancements

- Add more tools and integrations
- Improve task planning and validation
- Add user authentication
- Support more file formats
- Add advanced memory capabilities

## Author

Developed as an AI Agent and Automation System project using Python, Groq API, and Streamlit.
