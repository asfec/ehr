from db import db

class DoctorModel(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(80) , nullable=False)
    dob =  db.Column(db.DateTime)
    phone = db.Column(db.String(12))
    email = db.Column(db.String(80))
    specialization = db.Column(db.String(80))
    
    record = db.relationship("RecordModel" , back_populates="doctor")
    user = db.relationship("UserModel", back_populates="doctor" , cascade="all, delete")
    