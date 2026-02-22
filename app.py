from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Dockerized Python App!", "status": "Active"})

@app.route('/health')
def health():
    # Սա Kubernetes-ի համար է, որ տեսնի ծրագիրը ողջ է թե ոչ
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)