
from flask import Flask, request, jsonify
from state_registry_scraper_starter import get_registry_info

app = Flask(__name__)

@app.route('/enrich', methods=['POST'])
def enrich():
    data = request.get_json()
    company_name = data.get("company_name")
    state = data.get("state")

    if not company_name or not state:
        return jsonify({"error": "Missing company_name or state"}), 400

    result = get_registry_info(company_name, state)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
