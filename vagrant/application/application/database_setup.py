# Setup the database for the inventory system
# Attention: This overrides the existing file and deletes all tables
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import MetaData
 
Base = declarative_base()
 
class StockItem(Base):
    __tablename__ = 'stockitem'
   
    upc = Column(Integer, primary_key=True)
    productname = Column(String(250), nullable=False)
    manufacturer = Column(String(250))
    quantity = Column(Integer, nullable=False)
    size = Column(String(15))

engine = create_engine('sqlite:///file:stocks?check_same_thread=False&uri=True')
 

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

meta = MetaData(bind=engine, reflect=True)
for table in reversed(meta.sorted_tables):
    session.execute(table.delete())
session.commit()