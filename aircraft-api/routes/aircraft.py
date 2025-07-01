from flask import Blueprint, jsonify
from services.readsb_service import fetch_aircraft_data

aircraft_bp = Blueprint("aircraft", __name__)

@aircraft_bp.route("/count", methods=["GET"])
def aircraft_count():
    try:
        data = fetch_aircraft_data()
        aircraft_list = data.get("aircraft", [])
        return jsonify({"aircraft_count": len(aircraft_list)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
