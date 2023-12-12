from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from enum import Enum

app = FastAPI()

class Role(str, Enum): # (Enum) it will works like htmp option tag/element 
    ADMIN = 'ADMIN'
    USER  = 'USER'
    NAME  = 'NAME'
    CITY  = 'CITY'

@app.get('/user/{role}')
async def user(role : Role):
    print(role)
    return JSONResponse(status_code= status.HTTP_200_OK, content = {
        'other' : role,
        'name' : 'sagor ahmed',
        'city' : 'Tangail',
        'country' : 'Bangladesh'
    })
    
    
# @app.get('/user/{any}')
# async def user(any : Role):
#     # print(any)
#     return JSONResponse(status_code= status.HTTP_200_OK, content = {
#         'other' : any,
#         'name' : 'sagor ahmed',
#         'city' : 'Tangail',
#         'country' : 'Bangladesh'
#     })
    
