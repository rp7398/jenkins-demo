from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

@api.route("/add/<int:a>/<int:b>", methods=["GET"])
def add(a, b):
    return jsonify({"result": a + b})
