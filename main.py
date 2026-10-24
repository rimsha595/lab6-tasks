import os
from flask import Flask, jsonify, request

app = Flask(__name__)
TASKS = []

@app.get("/")
def home():
    return jsonify(
        service="tasks-api",
        version=os.getenv("GAE_VERSION", "local")
    )

@app.post("/tasks")
def add_task():
    TASKS.append(request.get_json())
    return jsonify(count=len(TASKS)), 201

@app.get("/tasks")
def list_tasks():
    return jsonify(TASKS)
