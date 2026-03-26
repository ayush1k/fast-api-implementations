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

patient_dict = {'name':'Ayush','gender':'Male','age':'24','address':address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)

temp = patient1.model_dump()
print(temp)
print(type(temp))