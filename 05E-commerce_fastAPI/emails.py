from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from dotenv import dotenv_values
from typing import List
from models import User
import jwt

config_credential = dotenv_values(".env")

conf = ConnectionConfig(
    MAIL_USERNAME = config_credential["EMAIL"],
    MAIL_PASSWORD = config_credential["PASSWORD"],
    MAIL_FROM = config_credential["EMAIL"],
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",


)

class EmailSchema(BaseModel):
    email : List[EmailStr]
    
async def send_email(email : List, instance : User):
    token_data = {
        'id' : instance.id,
        'username' : instance.username
    }
    
    token = jwt.encode(token_data, config_credential['SECRET'], algorithm='HS256') # make jwt token with id, username, secret token
    
    template = f"""

        <!DOCTYPE html>
        <html>
            <head>
            
            </head>
            
            <body>
                <div style="text-align: center; justify-content: center; display: flex, flex-direction: column">
                    <h3>Account Verification</h3>
                    <br>
                    <p>Thanks for choosing the shop ! Please click on the button below to verify your account</p>
                    
                    <a style="margin-top: 1rem, padding: 1rem, border-radius: 0.5rem, 
                    font-size: 1rem, text-decoration: none; background: #0275d8; color: white; 
                    href="http://localhost:8000/verification/?token={token}" ">Verify your email</a> 
                      
                    <p>Kindly ignore this email if you did not register in the shop !</p>                 
                </div>
            </body>
        </html>
    
    """
    
    message = MessageSchema(
        subject = 'Shop account verification email',
        recipients = email, # List of recipient
        body = template,
        subtype = 'html'
    )
    
    fm = FastMail(conf)
    await fm.send_message(message= message)