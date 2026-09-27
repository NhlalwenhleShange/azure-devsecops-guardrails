from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "azure-devsecops-guardrails",
        "version": "1.0.0"
    }), 200


@app.route('/api/telemetry', methods=['GET'])
def get_telemetry():
    return jsonify({
        "device_id": "esp32-sensor-01",
        "temperature": 24.5,
        "humidity": 60.2,
        "status": "active"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)