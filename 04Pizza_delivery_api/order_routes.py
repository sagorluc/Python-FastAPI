from fastapi import status, APIRouter
from fastapi.responses import JSONResponse

order_router = APIRouter()

@order_router.get('/order')
async def test_order():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        'order' : 'everything is okay from order'
    })
