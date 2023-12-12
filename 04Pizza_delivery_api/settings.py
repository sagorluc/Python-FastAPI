from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key : str = '7a4674aaaecf8adbdcf5f03d2e10990e75f337e1d0d1fdb95e8b2d651a71070a'
     