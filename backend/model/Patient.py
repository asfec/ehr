from db import db

class PatientModel(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(80) , nullable=False)
    dob =  db.Column(db.DateTime)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(80))
    phone = db.Column(db.String(12) , nullable=False)
    email = db.Column(db.String(80))
    
    record = db.relationship("RecordModel", back_populates="patient" , lazy="dynamic" , cascade="all, delete")
    appointment = db.relationship("AppointmentModel", back_populates="patient" , lazy="dynamic" , cascade="all, delete")
    user = db.relationship("UserModel", back_populates="patient"  , cascade="all, delete")