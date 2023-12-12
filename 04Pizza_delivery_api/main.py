from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from auth_routes import auth_router
from order_routes import order_router
from login_routes import login_router
from fastapi_jwt_auth import AuthJWT
from settings import Settings 

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(order_router)
# app.include_router(login_router)


@app.get('/')
async def test_main():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        'name' : 'sagor',
        'city' : 'Tangail'
    })