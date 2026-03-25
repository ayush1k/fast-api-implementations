from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str 
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain name')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')
        #Modes (before vs after): By default, validators run after Pydantic coerces the type. If you set @field_validator("age", mode="before"), it will receive the raw, un-coerced data (e.g., the string "30" instead of the integer 30).

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
                'age':24, 
                'email':'ayush@icici.com',
                'weight':70, 
                'married':False, 
                'allergies':['pollen','dust'], 
                'contact_details': {'email':'ayushkumar47834@gmail.com', 'phone':'8318530390'}
                }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)