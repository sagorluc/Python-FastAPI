from pydantic import BaseModel
from typing import Optional

class SignUp(BaseModel):
    id        : Optional[int]
    username  : str
    email     : str
    password  : str
    is_active : Optional[bool]
    is_staff  : Optional[bool] 
    
    class Config: # just for default user creation. it's an optional
        orm_mode = True
        schema_extra = {
            
            'example' : {
                'username'  : 'sagor ahmed',
                'email'     : 'sagor@gmail.com',
                'password'  : 'password',
                'is_active' : True,
                'is_staff'  : False
            },
        }
    
    

class Login(BaseModel):
    username : str
    password : str
    