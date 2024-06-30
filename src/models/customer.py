from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.dbs.postgres import Base


class Customer(Base):

    __tablename__ = "customer"
    
    customer_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address_id = Column(Integer, nullable=False)
    activebool = Column(Boolean, nullable=False)
    create_date = Column(DateTime, nullable=False)
    last_update = Column(DateTime, nullable=False)
    active = Column(Integer, nullable=False)