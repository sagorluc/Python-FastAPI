from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    id          = fields.IntField(pk= True, index=True)
    username    = fields.CharField(max_length=25, null=False, unique=True)
    email       = fields.CharField(max_length=25, null=False, unique=True)
    password    = fields.CharField(max_length=250, null=False)
    is_verified = fields.BooleanField(default=False)
    join_date   = fields.DatetimeField(auto_add_now= True, default=datetime.utcnow)
 
    
    
class Business(Model):
    id               = fields.IntField(pk= True, index= True)
    business_name    = fields.CharField(max_length=25, null=False, unique=True)
    city             = fields.CharField(max_length=25, null=False, default="Unspacified")
    region           = fields.CharField(max_length=25, null=False,  default="Unspacified")
    bus_descriptio   = fields.TextField()
    logo             = fields.CharField(max_length=25, null=False,  default="png")
    bus_owner        = fields.ForeignKeyField('models.User', related_name= 'business' )
    

class Product(Model):
    id                  = fields.IntField(pk= True, index= True)
    product_name        = fields.CharField(max_length=25, null=False, index=True)
    category            = fields.CharField(max_length=25, null=False)
    original_price      = fields.DecimalField(max_digits=12, decimal_places=2)
    discount_price      = fields.DecimalField(max_digits=12, decimal_places=2)
    discount_persentage = fields.IntField()
    offer_expire_date   = fields.DateField(default= datetime.utcnow)
    product_image       = fields.CharField(max_length=100, null=True, default="productDefault.png")
    business            = fields.ForeignKeyField('models.Business', related_name="products")
    

# Dont showing the spacific fields to user   
user_pydantic = pydantic_model_creator(User, name='User', exclude=('is_verified', ))
user_pydanticIn = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, exclude=('is_verified', 'join_date'))
user_pydanticOut = pydantic_model_creator(User, name='UserOut', exclude=('password', ))

business_pydantic = pydantic_model_creator(Business, name='Business')
business_pydanticIn = pydantic_model_creator(Business, name='BusinessIn', exclude_readonly=True)

product_pydantic = pydantic_model_creator(Product, name="Product")
product_pydanticIn = pydantic_model_creator(Product, name="ProductIn", exclude= ("discount_persentage", "id"))
