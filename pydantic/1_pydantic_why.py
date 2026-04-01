from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # name: str = Field(max_length=50) # the maximum length in the name will be 50
    name: Annotated[str, Field(max_length=50, title = 'Name of the patient', description='Give the name of the patient in less that 50 characters', examples=['Ayush Kumar','Nitish Singh'])]
    
    age: int = Field(gt=0, lt=120) # now the value will always be greater than 0 and less that 120
    
    email: EmailStr  
    
    Linkedin_url: AnyUrl
    
    # weight: float # pydantic is smart enough to understand that even if we pass a number in a string it will also accept it so in order to not let it happen we do the following
    weight: Annotated[float, Field(strict=True)]
    
    # married: Optional[bool] = None #optional is used to create a field which is optional and also we have to provide a null value by default
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    
    allergies: List[str] = 'No allergies' # takes a list of strings -- we can also put default values like this in all the feilds
    # if we just wrote list here we would only be able to check whether there is a list passed or not we will not be able to see if the list contains string values
    
    contact_details: Dict[str, str] # dictionary where key and value both are strings
    #the reason of using Dict instead of dict is same as the above reason
    # we can say for 2 level validation we are using Dict and List from typing module

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted")
    
def updateS_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("data inserted")
    
patient_info = {
                'name':'Ayush',
                'age':24, 
                'email':'ayushkumar47834@gmail.com',
                'Linkedin_url':'http://www.likedin.com/ayushhhhh',
                'weight':70, 
                'married':False, 
                'allergies':['pollen','dust'], 
                'contact_details': {'email':'ayushkumar47834@gmail.com', 'phone':'8318530390'}
                }

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
