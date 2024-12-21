from flask.views import MethodView
from flask_smorest import abort ,Blueprint
from schemas import AppointmentSchema 
from sqlalchemy.exc import SQLAlchemyError
from db import db

from model import AppointmentModel  , PatientModel 
from flask_jwt_extended import jwt_required

blp = Blueprint('Appointment' ,'appointment' , description = 'Operations on appointment')

@blp.route('/patient/<string:patient_id>/appointment')
class PatientAppointment(MethodView):
    @jwt_required()
    @blp.response(200 , AppointmentSchema(many=True))
    def get(self , patient_id):
        patient = PatientModel.query.get_or_404(patient_id)
        return patient.appointments.all()
    
@blp.route('/appointment')
class AppointmentList(MethodView):
    @jwt_required()
    @blp.response(200 , AppointmentSchema(many=True))
    def get(self):
        return AppointmentModel.query.all()
    
    @jwt_required()
    def delete(self , appointment_id):
        appointment = AppointmentModel.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return {'message ' : 'appointment delete successfully'}
    
    @blp.arguments(AppointmentSchema)
    @blp.response(201 , AppointmentSchema)
    @jwt_required()
    def post(self , appointment_data):
        appointment = AppointmentModel(**appointment_data)
        try:
            db.session.add(appointment)
            db.session.commit()
        except SQLAlchemyError:
            abort(500 , message = 'An error occurred while inserting the appointment')
        return appointment
     
    
    