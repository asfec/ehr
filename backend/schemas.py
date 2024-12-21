from marshmallow import Schema, fields

class PlainPatientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dob = fields.Date()
    gender = fields.Str()
    address = fields.Str()
    phone = fields.Str(required=True)
    email = fields.Str()
    
class PlainDoctorSchema(Schema):
    id = fields.Int(dump_only=True) 
    name = fields.Str(required=True)
    dob = fields.Date()
    phone = fields.Str()
    email = fields.Str()
    specialization = fields.Str()
    
class PlainRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    record_date = fields.Date(required=True)
    symptom = fields.Str()
    diagnosis = fields.Str()
    treatment_plan = fields.Str()
    note = fields.Str()
    
class PlainPrescriptionSchema(Schema):
    id = fields.Int(dump_only=True)
    medicine_name = fields.Str(required=True)
    dosage = fields.Str(required=True)
    frequency = fields.Str(required=True)
    duration = fields.Str()
    
class PlainAppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    appointment_date = fields.Date(required=True)
    note = fields.Str()
    
    
    
class PatientSchema(PlainPatientSchema):
    pass

class DoctorSchema(PlainDoctorSchema):
    pass

class RecordSchema(PlainRecordSchema):
    patient = fields.Nested(PlainPatientSchema(), dump_only=True)
    doctor = fields.Nested(PlainDoctorSchema(), dump_only=True)
    
class PrescriptionSchema(PlainPrescriptionSchema):
    record_id = fields.Nested(PlainRecordSchema(), dump_only=True)
    
class AppointmentSchema(PlainAppointmentSchema):
    patient = fields.Nested(PlainPatientSchema(), dump_only=True)
    

class RecordUpdateSchema(Schema):
    record_date = fields.Date()
    symptom = fields.Str()
    diagnosis = fields.Str()
    treatment_plan = fields.Str()
    note = fields.Str()
    
class PrescriptionUpdateSchema(Schema):
    medicine_name = fields.Str()
    dosage = fields.Str()
    frequency = fields.Str()
    duration = fields.Str()
    
class AppointmentUpdateSchema(Schema):
    appointment_date = fields.Date()
    note = fields.Str()

class PatientUpdateSchema(Schema):
    name = fields.Str(required=True)
    dob = fields.Date()
    gender = fields.Str()
    address = fields.Str()
    phone = fields.Str(required=True)
    email = fields.Str()
    
class DoctorUpdateSchema(Schema):
    name = fields.Str(required=True)
    dob = fields.Date()
    phone = fields.Str()
    email = fields.Str()
    specialization = fields.Str()
    
class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str(required=True)

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)