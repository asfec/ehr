from db import db

class PrescriptionModel(db.Model):
    __tablename__ = "prescription"
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey("record.id"), nullable=False)
    medicine_name = db.Column(db.String(80), nullable=False)
    dosage = db.Column(db.String(80), nullable=False)
    frequency = db.Column(db.String(80), nullable=False)
    note = db.Column(db.String(255))
    
    record = db.relationship("RecordModel", back_populates="prescription")