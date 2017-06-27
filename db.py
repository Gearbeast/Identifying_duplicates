from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///perriconemd.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Product(Base):
    __table__ = 'product'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, unique=True)
    product_name = Column (String(100))
    product_price = Column(Integer)
    product_description = Column(Text)
    product_details = Column(Text)
    key_sciences = Column(Text)
    ingredients = Column(Text)
    application = Column(Text)