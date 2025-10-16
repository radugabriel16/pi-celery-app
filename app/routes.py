from flask import Blueprint, request, jsonify
from celery.result import AsyncResult
from .tasks import calculate_pi
from . import celery

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/", methods=["GET"])
def home_page():
    message = "Hello! You are ready to test the app!"
    return message, 202

@routes_bp.route("/calculate_pi", methods=["GET"])
def calculate_pi_route():
    try:
        n = int(request.args.get("n", 0))
        if n <= 0:
            raise ValueError

        task = calculate_pi.apply_async(args=[n])
        return jsonify({"task_id": task.id}), 202

    except ValueError:
        return jsonify({"error": "Invalid parameter 'n'"}), 400


@routes_bp.route("/check_progress", methods=["GET"])
def check_progress():
    task_id = request.args.get("task_id")
    if not task_id:
        return jsonify({"error": "Missing 'task_id' parameter"}), 400

    task = AsyncResult(task_id, app=celery)

    if task.state == "PROGRESS":
        progress = task.info.get("progress", 0)
        return jsonify({ "state": "PROGRESS","progress": progress,"result": None }), 202

    elif task.state == "SUCCESS":
        return jsonify({ "state": "FINISHED","progress": 1.0,"result": task.result }), 200

    else:
        return jsonify({ "state": task.state,"progress": 0,"result": None }), 202
