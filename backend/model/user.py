from db import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(10), nullable=False)

    doctor = db.relationship("DoctorModel", back_populates="user", lazy="dynamic", cascade="all, delete")
    patient = db.relationship("PatientModel", back_populates="user", lazy="dynamic", cascade="all, delete")