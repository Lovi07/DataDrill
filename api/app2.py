import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from query_api import run_query

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to DataDrill API!"})

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    question = data.get("text")

    if not question:
        return jsonify({"error": "Missing 'text' in request"}), 400

    result = run_query(question)

    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    return jsonify({
        "query": question,
        "sql": result["sql"],
        "columns": result["columns"],
        "rows": result["rows"]
    })

if __name__ == "__main__":
    app.run(debug=True)
