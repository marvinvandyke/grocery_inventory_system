from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from database_setup.database_setup import Base, StockItem
import foodrepowrapper.foodrepo_API as foodAPI

# Create flask application
app = Flask(__name__)

# Setup database session
engine=create_engine('sqlite:///database_setup/stocks.db?check_same_thread=False')
Base.metadata.bind=engine
session_factory=sessionmaker(bind=engine)
DBSession = scoped_session(session_factory)
session = DBSession()

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
        return jsonify(productInfo)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug=True
    app.run(host='0.0.0.0', port=5000)