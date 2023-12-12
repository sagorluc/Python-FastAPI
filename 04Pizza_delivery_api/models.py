from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.types import ChoiceType
from sqlalchemy_utils import ChoiceType



ORDER_STATUS = (
    ('PENDING', 'PENDING'),
    ('IN-TRANSIT', 'IN-TRANSIT'),
    ('DELIVERED', 'DELIVERED'),
)

PIZZA_SIZES = (
    ('SMALL', 'SMALL'),
    ('MEDIUM', 'MEDIUM'),
    ('LEARGE', 'LEARGE'),
    ('EXTRA-LEARGE', 'EXTRA-LEARGE')
)

class User(Base):
    __tablename__ = 'user'
    id        = Column(Integer, primary_key=True)
    username  = Column(String(25), unique= True)
    email     = Column(String(30), unique= True)
    password  = Column(Text, nullable= True)
    is_active = Column(Boolean, default= False)
    is_staff  = Column(Boolean, default= False)
    orders    = relationship('Order', back_populates='user')
    
    def __str__(self):
        return f"< User {self.username}"
    
    
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable= True)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default='ORDER STATUS')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default='PIZZA SIZE')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')
    
    def __str__(self):
        return f"> Order {self.id}"
    
    