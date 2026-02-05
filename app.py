from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_message
    )

    return jsonify({
        "reply": response.output_text
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
