from passlib.context import CryptContext
from dotenv import dotenv_values
from fastapi.responses import HTMLResponse
from fastapi import status, HTTPException
from models import User
import jwt

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_hashed_password(password):
    return password_context.hash(password)


config_credential = dotenv_values('.env')

async def verify_token_decode(token : str):
    try:
        pay_load = jwt.decode(token, config_credential['SECRET'], algorithm=['HS256'])
        user = User.get(id = pay_load.get('id'))
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token", 
                            headers={"WWW-Authenticate": "Bearer"})
        
    return user