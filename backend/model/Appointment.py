from db import db


class AppointmentModel(db.Model):
    __tablename__ = "appointment"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))
    date = db.Column(db.DateTime)
    note = db.Column(db.String(255))
    
    patient = db.relationship("PatientModel", back_populates="appointment")