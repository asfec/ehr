from flask.views import MethodView
from flask_smorest import abort ,Blueprint
from schemas import RecordSchema , RecordUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db

from model import RecordModel , DoctorModel , PatientModel


blp = Blueprint('Record' ,'record' , description = 'Operations on record')


@blp.route('/doctor/<string:doctor_id>/record')
class RecordDoctor(MethodView):
    @blp.response(200 , RecordSchema(many=True))
    def get(self , doctor_id):
        doctor = DoctorModel.query.get_or_404(doctor_id)
        return doctor.records.all()
    
    @blp.arguments(RecordSchema)
    @blp.response(201 , RecordSchema)
    def post(self , record_data , doctor_id):
        record = RecordModel(**record_data , doctor_id = doctor_id)
        
        try:
            db.session.add(record)
            db.session.commit()
        except SQLAlchemyError:
            abort(500 , message = 'An error occurred while inserting the record')
        return record
@blp.route('/doctor/<string:doctor_id>/record/<string:record_id>')
class RecordfromDoctor(MethodView):
    @blp.response(200 , RecordSchema)
    def get(self , record_id):
        record = RecordModel.query.get_or_404(record_id)
        return record
    
    def delete(self , record_id):
        record = RecordModel.query.get_or_404(record_id)
        db.session.delete(record)
        db.session.commit()
        return {'message ' : 'record delete successfully'}
    
    @blp.arguments(RecordUpdateSchema)
    @blp.response(200 , RecordSchema)
    def put(self , record_data  , record_id):
        record = RecordModel.query.get_or_404(record_id)
        if record :
            record.diagnosis = record_data['diagnosis']
            record.treatment = record_data['treatment']
            record.prescription = record_data['prescription']
            record.date = record_data['date']
        else :
            record = RecordModel(id = record_id , **record_data)
        db.session.add(record)
        db.session.commit()
        
        return record

@blp.route('/patient/<string:patient_id>/record')
class PatientRecord(MethodView):
    @blp.response(200 , RecordSchema(many=True))
    def get(self , patient_id):
        patient = PatientModel.query.get_or_404(patient_id)
        return patient.records.all()
    
@blp.route('/record/<string:record_id>')
class Tag(MethodView):
    @blp.response(200 , RecordSchema)
    def get(self , record_id):
        record = RecordModel.query.get_or_404(record_id)
        return record
    
    def delete(self , record_id):
        record = RecordModel.query.get_or_404(record_id)
        db.session.delete(record)
        db.session.commit()
        return {'message ' : 'record delete successfully'}
    
    @blp.arguments(RecordUpdateSchema)
    @blp.response(200 , RecordSchema)
    def put(self , record_data , record_id):
        record = RecordModel.query.get_or_404(record_id)
        if record :
            record.diagnosis = record_data['diagnosis']
            record.treatment = record_data['treatment']
            record.prescription = record_data['prescription']
            record.date = record_data['date']
        else :
            record = RecordModel(id = record_id , **record_data)
        db.session.add(record)
        db.session.commit()
        
        return record