from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)
API_ENDPOINT = "https://langchain-chatbot-6fpc.onrender.com/ask"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        question = request.json.get('question')
        if not question:
            return jsonify({"error": "No question provided"}), 400
            
        response = requests.post(
            API_ENDPOINT,
            json={"question": question},
            timeout=10
        )
        
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": "API request failed"}), 500
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', False))