from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

        # DB_prototype -> DB_username -> DB_password -> DB_host -> DB_name
db_url = "postgresql://sagor:102030@localhost/Pizza_delivery"
engine = create_engine(db_url, echo=True)

Base = declarative_base()
Session = sessionmaker()