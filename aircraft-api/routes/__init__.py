from .aircraft import aircraft_bp

def register_routes(app):
    app.register_blueprint(aircraft_bp, url_prefix="/aircraft")
