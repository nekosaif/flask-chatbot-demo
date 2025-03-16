from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
API_ENDPOINT = os.getenv('BACKEND_URL')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        question = request.json.get('question')
        response = requests.post(
            API_ENDPOINT,
            json={"question": question},
            timeout=10
        )
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))