from fastapi import APIRouter, HTTPException, status
from models import *
from authentication import get_hashed_password, verify_token_decode
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from emails import send_email


registration_router = APIRouter()

# signals
from tortoise.signals import post_save
from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient



@post_save(User)
async def create_business(
    sender : "Type[User]",
    instance : User,
    created : bool,
    using_db :"Optional[BaseDBAsyncClient]",
    update_fields : List[str] ) -> None:
    
    if created:
        business_obj = await Business.create(
            business_name = instance.username, bus_owner = instance)
        
        await business_pydantic.from_tortoise_orm(business_obj)
        
        # sent the email
        await send_email([instance.email], instance)


@registration_router.post('/registration')
async def my_registration(cur_user: user_pydanticIn):
    user_info = cur_user.dict(exclude_unset=True)
    user_info['password'] = get_hashed_password(user_info['password'])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    
    return {
        'status' : 'ok',
        'data' : f"Hello {new_user.username} !. Check you email inbox and click the link to confirm your registration"
    }


templates = Jinja2Templates(directory = "templates")
@registration_router.get('/verification', response_class=HTMLResponse)
async def email_verification(request : Request, token : str):
    user = await verify_token_decode(token)
    
    if user and not user.is_verified:
        user.is_verified = True
        await user.save()
        return templates.TemplateResponse("verification.html", {"request": request, "username": user.username})
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")