from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_schedule(schedule):
    """Ensure the schedule follows correct structure"""
    required_keys = ['time', 'task', 'reason']
    return all(
        isinstance(item, dict) and
        all(key in item for key in required_keys)
        for item in schedule
    )

@app.route('/api/plan', methods=['POST'])
def generate_schedule():
    try:
        data = request.get_json()
        print("data", data)

        if 'text' not in data or not data['text'].strip():
            return jsonify({"error": "Please describe your tasks"}), 400

        text = data['text'].strip()

        # Directly use the provided text as the prompt
        prompt = f"""
        Create a detailed daily schedule from the following plan description:

        {text}

        Consider the following guidelines:
        - Typical daily rhythms (e.g., meals, exercise, sleep)
        - Task nature (physical, mental, preparation)
        - Logical sequence (shower after gym)
        - Time-sensitive requirements (meals, meetings)

        Time Guidelines:
        - Meals: Breakfast (7-9 AM), Lunch (12-1 PM), Dinner (6-8 PM)
        - Exercise: Morning (6-8 AM) or Evening (5-7 PM)
        - Meetings: Typically 9 AM-5 PM
        - Self-care: Evening hours

        Return the schedule in JSON format with time in HH:MM AM/PM format.
        Example:
        {{
            "schedule": [
                {{"time": "7:00 AM", "task": "Breakfast", "reason": "..."}}
            ]}}
        """

        print("Generated prompt:", prompt)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert daily planner that outputs valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )

        # Parse and validate response
        result = json.loads(completion.choices[0].message.content)
        print("LLM Response:", result)

        if not validate_schedule(result.get('schedule', [])):
            return jsonify({"error": "Invalid schedule format"}), 500

        return jsonify(result)

    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse schedule response"}), 500
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Schedule generation failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
