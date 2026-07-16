from flask import Flask, jsonify
import os
import socket
from database import create_tables

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "service": "Task Manager API",
        "status": "running",
        "hostname": socket.gethostname()
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/config")
def config():
    return jsonify({
        "environment": os.getenv("APP_ENV"),
        "database": os.getenv("DB_HOST")
    })

print("BEFORE CREATE TABLES")
create_tables()
print("AFTER CREATE TABLES")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
