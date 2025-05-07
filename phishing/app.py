import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
@cross_origin(supports_credentials=True)
@app.route('/data', methods=['POST'])
def receive_data():
    """
    Endpoint to receive JSON data via POST request.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    try:
        data = request.get_json()
        file = open("data.json", "w")
        file.write(str(data))
        file.close()

        return jsonify({"message": "Data received successfully!", "yourData": data}), 200

    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"error": "An error occurred processing your request"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)