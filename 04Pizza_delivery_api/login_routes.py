from signup_login_models import Login
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from werkzeug.security import  check_password_hash
from fastapi_exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from auth_routes import auth_router
from database import Session
from models import User

# login_router = APIRouter(prefix="/login", tags="login")


@auth_router.post('/login')
async def log_in(cur_user : Login, Authorize: AuthJWT=Depends()):
    
    db_user = Session.query(User).filter(User.username == cur_user.username).first()
    
    check_password = check_password_hash(db_user.password , cur_user.password)
    
    if db_user.username != cur_user.username:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User does not found')
    
    if db_user and check_password:
       access_token = Authorize.create_access_token(subject= db_user.username)
       refresh_token = Authorize.create_refresh_token(subject= db_user.username)
       
       response = {
           'access_token' : access_token,
           'refresh_token' : refresh_token
       }

       return jsonable_encoder(response)
   
    raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="Invalid username or password")
        