from flask.views import MethodView
from flask_smorest import abort ,Blueprint
from schemas import PrescriptionSchema , PrescriptionUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from db import db

from model import PrescriptionModel , RecordModel

blp = Blueprint('Prescription' ,'prescription' , description = 'Operations on prescription')


@blp.route('/record/<string:record_id>/prescription')  
class RecordPrescription(MethodView):
    @blp.response(200 , PrescriptionSchema(many=True))
    def get(self , record_id):
        record = RecordModel.query.get_or_404(record_id)
        return record.prescriptions.all()
    
    @blp.arguments(PrescriptionSchema)
    @blp.response(201 , PrescriptionSchema)
    def post(self , prescription_data , record_id):
        prescription = PrescriptionModel(**prescription_data , record_id = record_id)
        
        try:
            db.session.add(prescription)
            db.session.commit()
        except SQLAlchemyError:
            abort(500 , message = 'An error occurred while inserting the prescription')
        return prescription
    
@blp.route('/record/<string:record_id>/prescription/<string:prescription_id>')
class PrescriptionfromRecord(MethodView):
    @blp.response(200 , PrescriptionSchema)
    def get(self , prescription_id):
        prescription = PrescriptionModel.query.get_or_404(prescription_id)
        return prescription
    
    def delete(self , prescription_id):
        prescription = PrescriptionModel.query.get_or_404(prescription_id)
        db.session.delete(prescription)
        db.session.commit()
        return {'message ' : 'prescription delete successfully'}
    
    @blp.arguments(PrescriptionUpdateSchema)
    @blp.response(200 , PrescriptionSchema)
    def put(self , prescription_data  , prescription_id):
        prescription = PrescriptionModel.query.get_or_404(prescription_id)
        if prescription :
            prescription.drug = prescription_data['drug']
            prescription.dosage = prescription_data['dosage']
            prescription.frequency = prescription_data['frequency']
            prescription.duration = prescription_data['duration']
        else :
            prescription = PrescriptionModel(id = prescription_id , **prescription_data)
        db.session.add(prescription)
        db.session.commit()
        
        return prescription