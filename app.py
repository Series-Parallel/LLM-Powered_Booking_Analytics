#Task 4: (Part 2) Flask API integration on local machine

from flask import Flask, request, jsonify
import requests
import time


app = Flask(__name__)

COLAB_LLM_API = "https://2fa7-34-125-227-152.ngrok-free.app"

@app.route("/analytics", methods=["POST"])
def analytics():
    analytics_data = {
        "Total Revenue": 42723497.53,
        "Average ADR": 101.83,
        "Cancellation Rate": 0.37,
        "Most Popular Customer Type": "Transient"
    }
    return jsonify(analytics_data)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    response = requests.post(COLAB_LLM_API, json={"query": user_query})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get response from LLM"}), 500
    


if __name__ == "__main__":
    app.run(port=8000)