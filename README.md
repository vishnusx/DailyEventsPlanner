# Smart Daily Events Planner 🚀

A responsive web application that helps users optimally plan their day using AI-powered scheduling. Combines a React frontend with a Flask backend and OpenAI integration.

## Features ✨
- Add/Remove multiple tasks dynamically
- AI-generated daily schedule with time slots and reasoning
- Responsive design for all screen sizes
- Loading states and error handling
- Clean timeline visualization
- OpenAI GPT-3.5/4 integration for smart planning

## Technologies Used 💻
- **Frontend**: React, CSS3
- **Backend**: Python Flask
- **AI**: OpenAI API
- **Hosting**: Vercel (frontend) + Render (backend)
- **Build Tools**: npm, pip

## 🚀 Live Demo

    - 🔵 Frontend: [View React App](https://daily-events-planner.vercel.app/)
    - 🟣 Backend API: [View Flask API](https://dailyeventsplanner.onrender.com/api/plan)


## Installation locally 📦

### 🔹 Clone the Repo

```bash
git clone https://github.com/vishnusx/DailyEventsPlanner.git
cd DailyEventsPlanner
```

### Prerequisites
- Node.js (v14+)
- Python (v3.8+)
- OpenAI API key

### Backend Setup
1. Create a virtual environment:
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

2. Install Python dependencies:
    ```bash
    pip install flask flask-cors openai python-dotenv
    or
    pip install -r requirements.txt
    ```

### Frontend Setup
1. Install Node.js dependencies:
    ```bash
    cd client
    npm install
    ```

2. Create an environment file in the root directory or Backend:
    ```bash

    echo "OPENAI_API_KEY=your_api_key_here" > .env
    ```

### Running the Application locally 🏃
1. Start the backend (runs on port 5001 by default):
    ```bash
    cd backend
    python app.py
    ```

2. Start the frontend(client) (runs on port 3000 in a separate terminal):
    ```bash
    cd client
    npm start
    ```

## Project Structure 📂
DailyEventsPlanner/
├── backend/
│   ├── app.py               # Flask backend server
│   └── requirements.txt     # Backend dependencies
│
├── client/
│   ├── package.json         # Frontend dependencies
│   ├── package-lock.json    # Locked dependency versions
│   ├── public/              # React static assets
│   └── src/                 # React components
│       ├── App.js           # Main React component
│       ├── App.css          # Styling components
│       ├── index.js         # Entry point
│       └── ...              # Other React files (tests, helpers)
│
├── .env                     # Environment variables (ignored by Git)
├── .gitignore               # Files and folders to exclude from Git
└── README.md                # Project documentation

## Configuration ⚙️

1. Obtain an OpenAI API key from [OpenAI's platform](https://platform.openai.com).
2. Add it to the `.env` file:
    ```bash
    OPENAI_API_KEY=your_actual_key_here
    ```

"# DailyEventsPlanner"
