from flask import Blueprint, render_template,request,redirect,url_for,session,flash
from app.db_access import DataProductAccess
import datetime
from datetime import date
import random
import string
import json


cart_module = Blueprint("cart_module", __name__)


@cart_module.route("/addcart",methods=['GET','POST','PUT'])
def addcart():
    if request.method == "PUT":
        product_name = request.json['product_name']
        quantity = int(request.json['quantity'])
        image_link = request.json['image_link']
        price = int(request.json['price'])
        # quantity = request.json['quantity']
        # c = {'product_name':product_name,'quantity': quantity}
        # print(product_name)
        
        c = {'product_name':product_name,'image_link':image_link,'price':price,'quantity':quantity}
        list_of_all_values = [value for elem in session['cart_list'] for value in elem.values()]
        print(c)
        if c['product_name'] not in list_of_all_values:
            session['cart_list'].append(c)
        else:
            session['cart_list'] = [i for i in session['cart_list'] if not (i['product_name'] == c['product_name'])]
            session['cart_list'].append(c)
    if request.method == "POST":       
        return redirect(url_for("cart_module.cart"))
    return redirect(url_for("cart_module.cart"))


@cart_module.route("/shoppingcart",methods=['GET','POST'])
def cart():
    if request.method == "POST":
        product_quantity = request.form.getlist("product_quantity")
        print(product_quantity)
        for i in range(0,len(product_quantity)):
            if session['cart_list'][i]['quantity'] != product_quantity[i]:
                session['cart_list'][i]['quantity'] = product_quantity[i]
        print(session['cart_list'])
        return redirect(url_for("cart_module.checkout1"))
    try:
        if session["user_id"][0]:
            pass
    except:
        return redirect(url_for("user_module.login"))
    print(session['cart_list'])
    cart = []       
    try:
        for prod in session['cart_list']:
            print(prod)
            cart.append(prod)          
    except:
        cart = []
    db_connect = DataProductAccess()
    list_product = db_connect.get_product_by_table(1)
    if list_product != None:
        for item in list_product:
            c = {'product_name':item[2],'image_link':item[4],'price':item[3],'quantity':item[5]}
            cart.append(c)
    return render_template("pages/shoppingcart.html",cart=cart,quantity=str(len(cart)))

@cart_module.route("/delete/<string:product_name>")
def remove_product(product_name):
    # connect_db = DataProductAccess()
    # single_product = connect_db.get_singleproduct(product_name)
    # price = single_product[2]
    # image_path = single_product[5]
    session['cart_list'] = [i for i in session['cart_list'] if not (i['product_name'] == product_name)]
    return redirect(url_for("cart_module.cart"))

@cart_module.route("/checkout1",methods=['GET','POST'])
def checkout1():
    connect_db = DataProductAccess()
    cart = []       
    try:
        for prod in session['cart_list']:
            cart.append(prod)          
    except:
        cart = []
    if request.method == 'POST':
        today = date.today()
        email = request.form['email']
        fullname = request.form['fullname']
        address = request.form['address']
        phone = request.form['phone']
        order_date = today.strftime("%b-%d-%Y")
        delivery_date= (datetime.datetime.strptime(order_date, "%b-%d-%Y")+datetime.timedelta(days=4)).strftime("%b-%d-%Y")
        order_number = ''.join(random.choice(string.ascii_uppercase+ string.digits) for _ in range(9))
        user_id = session['user_id'][0]
        product_list = ""
        total = 0
        for i in session['cart_list']:
            product_list = product_list+str(i["quantity"])+" x "+str(i["product_name"])+"\n"
            total = total + int(i["quantity"])*int(i["price"])
        if email != None and phone != None and fullname != None:
            if connect_db.insert_order(user_id,fullname,email,address,phone,order_date,delivery_date,order_number,product_list,total):
                session['cart_list'] = []
                return render_template("pages/thankyou.html",email=email,fullname=fullname,address=address,phone=phone,order_date=order_date,delivery_date=delivery_date,order_number=order_number,cart=cart)
            else:
                flash("Error Connect!!!")
    return render_template("pages/checkout1.html",cart=cart,quantity=str(len(cart)))

# @cart_module.route("/checkout2")
# def checkout2():
#     return render_template("pages/checkout2.html")

# @cart_module.route("/checkout3")
# def checkout3():
#     return render_template("pages/checkout3.html")

# @cart_module.route("/thankyou")
# def thankyou():
#     return render_template("pages/thankyou.html")