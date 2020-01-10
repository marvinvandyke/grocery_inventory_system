from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from database_setup import Base, StockItem

engine = create_engine('sqlite:///stocks.db')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine)
session = DBSession()

stockItem1 = StockItem(upc=8076802085981, productname="Fusilli", manufacturer="Barilla", quantity=0, size="500g")
stockItem2 = StockItem(upc=4316734051161, productname="Organic Coconut Oil", manufacturer="bio asia", quantity=0, size="250ml")
session.add(stockItem1)
session.add(stockItem2)
session.commit()

test = session.query(StockItem).all()

for i in test:
  print(i.productname)