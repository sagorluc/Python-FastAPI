from fastapi import status, APIRouter, Depends
from fastapi.responses import JSONResponse
from database import Session, engine
from signup_login_models import SignUp
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter()

session = Session(bind=engine)


@auth_router.get('/auth')
async def test_auth():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        'auth' : 'everything is okay from auth'
    })




@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(cur_user: SignUp):
    db_email = session.query(User).filter(User.email==cur_user.email).first() # get email from db
    
    if db_email is not None:
       return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this email already exist')
    
    db_username = session.query(User).filter(User.username==cur_user.username).first() # get username from db
    
    if db_username is not None:
       return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this username already exist') 
   
    # print('line 33',user.username) # input username
    # print('line 33',user.email)    # input email
    # print('line 33',user.password) # input password
   
    new_user = User(
       username = cur_user.username,
       email = cur_user.email,
       password = generate_password_hash(cur_user.password),
       is_active = cur_user.is_active,
       is_staff = cur_user.is_staff
   )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

