from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the DevSecOps Capstone!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "capstone-app"})

if __name__ == '__main__':
    # Binding to 0.0.0.0 is required for Docker container networking
    app.run(host='0.0.0.0', port=5000)
