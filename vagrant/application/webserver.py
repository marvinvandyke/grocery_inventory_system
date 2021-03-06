from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import current_app as app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from vagrant.models.stockitem import StockItem
from vagrant import db
# from models.database_setup import Base, StockItem
from vagrant.services import foodrepo_API as foodAPI

# Create flask application
# app = Flask(__name__)

# Setup database session
# engine=create_engine('sqlite:///file:database_setup/stocks?check_same_thread=False&uri=True')
#Base.metadata.bind=engine
#session_factory=sessionmaker(bind=engine)
#DBSession = scoped_session(session_factory)
#session = DBSession()

@app.route('/index/')
def displayEntryPage():
    return render_template('index.html')

@app.route('/index/result/', methods=['GET', 'POST'])
def searchUPC():
    if request.method == 'POST':
        upc = request.form['upc']

        # Search in local database first
        # If found redirect to product page for editing

        # TODO

        # Search in external databases
        # If found redirect to create new item in local database page
        # If not found redirect to create new item from scratch in local database page
        productInfo = foodAPI.getProductByUPC(upc)
        # return jsonify(productInfo)
        print(upc)
        return redirect(url_for('createNewProduct', product_upc=upc))

@app.route('/index/<int:product_upc>/createnew/', methods=['GET', 'POST'])
def createNewProduct(product_upc):
    if request.method == 'GET':
        return render_template('createNewProduct.html', product_upc=product_upc)
    
    if request.method == 'POST':
        return redirect(url_for('displayEntryPage'))

# if __name__ == '__main__':
    #app.secret_key = 'super_secret_key'
    #app.debug=True
    #app.run(host='0.0.0.0', port=5000)