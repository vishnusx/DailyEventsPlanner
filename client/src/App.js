import { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [schedule, setSchedule] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (!inputText.trim()) {
        setError('Please describe your tasks');
        return;
      }

      const response = await fetch('https://dailyeventsplanner.onrender.com/api/plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText })
      });


      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setSchedule(data.schedule);
      }
    } catch (err) {
      setError('Failed to generate schedule. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>Smart Daily Events Planner 🚀</h1>

      <form onSubmit={handleSubmit}>
        <div className="text-input">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Describe your day's tasks (e.g. 'I need to exercise, prepare for the 2PM meeting, and help with homework after school')"
            rows="5"
          />
        </div>

        <div className="form-controls">
          <button type="submit" disabled={loading}>
            {loading ? 'Planning...' : 'Generate Smart Schedule ✨'}
          </button>
        </div>

        {error && <div className="error-message">{error}</div>}
      </form>

      {loading && <div className="spinner"></div>}

      {schedule && (
        <div className="schedule">
          <h2>Your Optimized Schedule 📅</h2>
          <div className="timeline">
            {schedule.map((item, index) => (
              <div key={index} className="timeline-item">
                <div className="timeline-time">{item.time}</div>
                <div className="timeline-content">
                  <h3>{item.task}</h3>
                  <p className="reason">📌 {item.reason}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
