from flask import Blueprint, render_template,session,request,redirect,url_for
from app.db_access import DataProductAccess
import math
index_module = Blueprint("index_module", __name__)


@index_module.route("/")
@index_module.route("/homepage")
def index():
    connect_db = DataProductAccess()
    per_page = 3
    
    # cart = []       
    # try:
    #     for prod in session['cart_list']:
    #         cart.append(prod)         q 
    # except:
    #     cart = []
    # print(cart)
    if 'cart_list' not in session:
        session['cart_list'] = []
    
    current_page = request.args.get('page',1)
    products = connect_db.count_product()
    page_limit = math.ceil(products/per_page)
    product_list = connect_db.get_product(per_page,int(current_page))
    return render_template("Pages/index.html",product_list = product_list, page_limit=page_limit,cart_list=session['cart_list'],num_of_product=len(session['cart_list']))#,cart=cart,quantity=str(len(cart))

@index_module.route("/channelDetail")
def channeldetail():
    connect_db = DataProductAccess()
    chef = request.args.get('chef')
    print(chef)
    product = connect_db.get_product_by_chef(chef)
    return render_template("pages/channelDetail.html",cart_list=session['cart_list'],num_of_product=len(session['cart_list']),products=product,chef=chef)

@index_module.route("/articles")
def articles():
    return render_template("pages/articles.html")

