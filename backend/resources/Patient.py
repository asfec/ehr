from flask.views import MethodView
from flask_smorest import abort ,Blueprint
from schemas import PatientSchema , PatientUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db

from model import PatientModel 


blp = Blueprint('Patient' ,'patient' , description = 'Operations on patient')


@blp.route('/patient/<string:patient_id>')
class Patient(MethodView):
    #lay thong tin benh nhan theo id
    @blp.response(200 , PatientSchema)
    def get(self , patient_id ):
        patient = PatientModel.query.get_or_404(patient_id)
        return patient
    
    #xoa benh nhan theo id
    def delete(self , patient_id):
        patient = PatientModel.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit
        return {'message ' : 'patient delete successfully'}
    
    #update thong tin
    @blp.arguments(PatientUpdateSchema)
    @blp.response(200 , PatientSchema)
    def put(self , patient_data , patient_id):
        patient = PatientModel.query.get_or_404(patient_id)
        if patient :
            patient.name = patient_data['name']
            patient.dob = patient_data['dob']
            patient.gender = patient_data['gender']
            patient.address = patient_data['address']
            patient.phone = patient_data['phone']
            patient.email = patient_data['email']
        else :
            patient = PatientModel(id = patient_id , **patient_data)
        db.session.add(patient)
        db.session.commit()
        
        return patient
    

@blp.route('/patient')
class PatientsList(MethodView):
        #lay danh sach benh nhan
    @blp.response(200 , PatientSchema(many=True))
    def get(self):
        return PatientModel.query.all()
        
        #them benh nhan
    @blp.arguments(PatientSchema)
    @blp.response(201 , PatientSchema)
    def post(self , patient_data):
        patient = PatientModel(**patient_data)
        try:
            db.session.add(patient)
            db.session.commit()
        except SQLAlchemyError:
            abort(500 , message="An error occurred while adding the patient")
        return patient 