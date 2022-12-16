from flask import Blueprint, render_template,request,redirect,url_for,session,flash
from app.db_access import DataProductAccess
import datetime
from datetime import date
import random
import string
import json


product_module = Blueprint("product_module", __name__)

@product_module.route("/productDetail/<string:product_name>")
def product_detail(product_name):
    connect_db = DataProductAccess()
    product = connect_db.get_singleproduct(product_name)
    
    return render_template("pages/productDetail.html",cart_list=session['cart_list'],item=product,num_of_product=len(session['cart_list']))