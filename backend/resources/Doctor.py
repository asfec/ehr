from flask.views import MethodView
from flask_smorest import Blueprint , abort
from schemas import DoctorSchema ,DoctorUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db
from flask_jwt_extended import jwt_required
from model import DoctorModel

blp = Blueprint('Doctor' ,'doctor' , description = 'Operations on doctor')


@blp.route('/doctor/<string:doctor_id>')
class Doctor(MethodView):
    @blp.response(200 , DoctorSchema)
    @jwt_required()
    def get(self , doctor_id ):
        doctor = DoctorModel.query.get_or_404(doctor_id)
        return doctor
    
    @jwt_required()
    def delete(self , doctor_id):
        doctor = DoctorModel.query.get_or_404(doctor_id)
        db.session.delete(doctor)
        db.session.commit
        return {'message ' : 'doctor delete successfully'}
    
    @jwt_required()
    @blp.arguments(DoctorUpdateSchema)
    @blp.response(200 , DoctorSchema)
    def put(self , doctor_data , doctor_id):
        doctor = DoctorModel.query.get_or_404(doctor_id)
        if doctor :
            doctor.name = doctor_data['name']
            doctor.dob = doctor_data['dob']
            doctor.phone = doctor_data['phone']
            doctor.email = doctor_data['email']
            doctor.specialization = doctor_data['specialization']
        else :
            doctor = DoctorModel(id = doctor_id , **doctor_data)
            
        db.session.add(doctor)
        db.session.commit()
        
        return doctor
    

@blp.route('/doctor')
class Doctorlist(MethodView):
    @jwt_required()
    @blp.response(200 , DoctorSchema(many=True))
    def get(self):
        return DoctorModel.query.all()
            
    @jwt_required()
    @blp.arguments(DoctorSchema)
    @blp.response(201 , DoctorSchema)
    def post(self , doctor_data):
        doctor = DoctorModel(**doctor_data)
        try:
            db.session.add(doctor)
            db.session.commit()
        except SQLAlchemyError:
            abort(500 , message = 'An error occurred while inserting the doctor')
        return doctor