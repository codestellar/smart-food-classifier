import requests
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gemini', methods=['POST'])
def gemini():
    data = request.get_json()
    category = data.get("category", "unknown")

    prompt = f"""
    A food image was classified as: {category}
    You are a smart food advisor AI. Please:
    1. Describe this category
    2. Say whether it's healthy or not
    3. Suggest 2 better alternatives if it's unhealthy
    4. Recommend one simple meal using it
    Keep it friendly and add emojis!
    """

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    response = requests.post(
        f"{GEMINI_ENDPOINT}",
        headers=headers,
        json=payload
    )

    gemini_output = response.json()
    try:
        text = gemini_output["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        text = "Sorry, something went wrong with Gemini."

    return jsonify({'advice': text})



if __name__ == '__main__':
    app.run(debug=True)
