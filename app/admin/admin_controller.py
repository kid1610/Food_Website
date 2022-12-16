from flask import Blueprint, render_template,request,redirect,url_for,session,flash
from app.db_access import DataProductAccess
import datetime
from datetime import date
import random
import string
import json
from werkzeug.utils import secure_filename
import os

admin_module = Blueprint("admin_module", __name__)

# @admin_module.route('/channelDashboard')
# def channel_dashboard():
#     # if session['role'] != [] :
#     #     if session['role'][0] == "admin":
#     #         return render_template("pages/channelDashboard.html",cart_list=session['cart_list'],num_of_product=len(session['cart_list']))
#     return redirect(url_for("user_module.login"))


@admin_module.route('/dashboard/<string:chef>',methods=["GET","POST"])
def channel_dashboard(chef):
    if session['role'] != [] :
        if session['role'][0] == "admin":
            connect_db = DataProductAccess()
            products = connect_db.get_product_by_chef(chef)
            print(products[2][5])
            if request.method == "POST":
                file = request.files['file_upload']
                filename = secure_filename(file.filename)
                file.save(os.path.join(r'E:\Workspace\Caps2\Smart_Order_System\food_website\app\static\images', filename))
                product_name = request.form['product_name']
                price  = request.form['price']
                time_order  = request.form['time_order']
                type_food = request.form['type_food']
                chef = chef
                story1 = request.form['story1']
                story2 = request.form['story2']
                story3 = request.form['story3']
                connect_db = DataProductAccess()
                connect_db.insert_product(product_name,price,time_order,type_food,filename,chef,story1,story2,story3)
            return render_template("pages/channelDashboard.html",cart_list=session['cart_list'],num_of_product=len(session['cart_list']),chef=chef, products=products)
    return redirect(url_for("user_module.login"))