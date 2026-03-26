from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

# using existing feilds to compute another feild 

class Patient(BaseModel):
    name: str 
    age: int
    email: EmailStr
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi

    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted")
    
def updates_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.bmi)
    print("data inserted")
    
patient_info = {
                'name':'ayush',
                'age':61, 
                'email':'ayush@icici.com',
                'weight':70, 
                'height':1.72,
                'married':False, 
                'allergies':['pollen','dust'], 
                'contact_details': {'email':'ayushkumar47834@gmail.com', 'phone':'8318530390'}
                }

patient1 = Patient(**patient_info)

updates_patient_data(patient1)