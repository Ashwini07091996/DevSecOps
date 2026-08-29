from flask import Flask, jsonify
import os
import subprocess

app = Flask(__name__)


@app.get("/")
def health():
    return jsonify({
        "service": "payment-api",
        "status": "running"
    })


@app.get("/health")
def health_check():
    return jsonify({"status": "healthy"})


@app.get("/config")
def config():
    return jsonify({
        "db_username": os.getenv("DB_USERNAME", "not-set"),
        "db_password": "********" if os.getenv("DB_PASSWORD") else "not-set"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


def run_command(user_input):
    result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
    return result.stdout
