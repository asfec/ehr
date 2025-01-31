from flask import Flask , jsonify  
from flask_smorest import Api
import os
from db import db

from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from resources.Patient import blp as  Patientblueprint
from resources.Doctor import blp as Doctorblueprint
from resources.Record import blp as Recordblueprint
from resources.Appointment import blp as Appointmentblueprint
from resources.Prescription import blp as Prescriptionblueprint
from resources.user import blp as Userblueprint

def create_app():
    app = Flask(__name__)
    
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    db_url = os.getenv("DB_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    api = Api(app)
    app.config["JWT_SECRET_KEY"] = "711685638168615895"
    jwt = JWTManager(app)
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
    with app.app_context():
        db.create_all()
        
    api.register_blueprint(Doctorblueprint)
    api.register_blueprint(Patientblueprint)
    api.register_blueprint(Recordblueprint)
    api.register_blueprint(Appointmentblueprint)
    api.register_blueprint(Prescriptionblueprint)
    api.register_blueprint(Userblueprint)
    return app
