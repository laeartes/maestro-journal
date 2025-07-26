from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import PracticeSession

sessions_bp = Blueprint("sessions", __name__)

@sessions_bp.route("/", methods=["POST"])
@jwt_required()
def add_session():
    data = request.get_json()
    user_id = int(get_jwt_identity())
    session = PracticeSession(
        user_id=user_id,
        instrument=data["instrument"],
        minutes=data["minutes"],
        notes=data.get("notes", "")
    )
    db.session.add(session)
    db.session.commit()
    return jsonify(message="Session added"), 201

@sessions_bp.route("/", methods=["GET"])
@jwt_required()
def get_sessions():
    user_id = int(get_jwt_identity())
    sessions = PracticeSession.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": s.id,
            "instrument": s.instrument,
            "minutes": s.minutes,
            "notes": s.notes,
            "date": s.date.isoformat()
        } for s in sessions
    ])

@sessions_bp.route("/<int:session_id>", methods=["DELETE"])
@jwt_required()
def delete_session(session_id):
    user_id = int(get_jwt_identity())
    session = PracticeSession.query.filter_by(id=session_id, user_id=user_id).first()
    if not session:
        return jsonify(message="Session not found"), 404
    db.session.delete(session)
    db.session.commit()
    return jsonify(message="Session deleted")
