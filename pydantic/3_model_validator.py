from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

# here we will create a model validator which will check if there is an emergency contact number in patient data then only a patient profile will be created 

class Patient(BaseModel):
    name: str 
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older that 60 must have an emergency contact number')
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted")
    
def updates_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted")
    
patient_info = {
                'name':'ayush',
                'age':61, 
                'email':'ayush@icici.com',
                'weight':70, 
                'married':False, 
                'allergies':['pollen','dust'], 
                'contact_details': {'email':'ayushkumar47834@gmail.com', 'phone':'8318530390','emergency':'8318530390'}
                }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)