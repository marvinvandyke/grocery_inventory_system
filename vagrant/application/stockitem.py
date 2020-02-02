from . import db

class StockItem(db.Model):
    __tablename__ = 'stockitem'
    
    upc = db.Model.Column(db.Model.Integer, primary_key=True)
    productname = db.Model.Column(db.Model.String(250), nullable=False)
    manufacturer = db.Model.Column(db.Model.String(250))
    quantity = db.Model.Column(db.Model.Integer, nullable=False)
    size = db.Model.Column(db.Model.String(15))