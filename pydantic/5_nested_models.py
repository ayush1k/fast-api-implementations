from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str
    

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
        
address_dict = {'city':'varanasi','state':'Uttar Pradesh','pin':'221002'}
address1 = Address(**address_dict)
