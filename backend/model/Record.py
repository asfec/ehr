from db import db
 
class RecordModel(db.Model):
    __tablename__ = "record"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)
    record_date = db.Column(db.DateTime , nullable=False)
    symptom = db.Column(db.String(255))
    diagnosis = db.Column(db.String(255))
    treament_plan = db.Column(db.String(255))
    note = db.Column(db.String(255))
    
    patient = db.relationship("PatientModel", back_populates="record")
    doctor = db.relationship("DoctorModel", back_populates="record")
    prescription = db.relationship("PrescriptionModel", back_populates="record")
        