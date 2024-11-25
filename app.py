from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query")
    # Mock response - Replace with actual query logic
    response = {"response": f"You asked: {user_query}. Answer: [Mock Answer]"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

