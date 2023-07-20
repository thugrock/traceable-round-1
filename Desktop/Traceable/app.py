from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Hello Traceable... Welcome to IIIT-Bangalore."
    elif request.method == 'POST':
        try:
            data = request.json
            print("Received data from POST request (from POSTMAN):", data)
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)
