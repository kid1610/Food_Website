from flask import Blueprint, render_template,request,redirect,url_for,session
from app.db_access import DataAccountAccess

user_module = Blueprint("user_module", __name__)
db = DataAccountAccess()

@user_module.route("/login",methods=['GET','POST'])
def login():
    error = None
    # if request.method == "GET":
    #     return render_template("Pages/login.html")
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        check = db.check_login(email,password)
        if check == True:
            session['user_id'] = db.get_user_id(email)
            session['role'] = db.get_role(email)
            if len(session['cart_list']) != 0:
                return redirect(url_for("cart_module.cart"))
            else:
                return redirect(url_for("index_module.index"))
        else:
            error = "Invalid Email or Password"
    return render_template("Pages/login.html",error= error)

@user_module.route("/register",methods=['GET','POST'])
def register():
    error = None
    # if request.method == "GET":
    #     return render_template("Pages/login.html")
    if request.method == "POST":
        username = str(request.form['fullname'])
        email = str(request.form['email'])
        password = str(request.form['password'])
        check = db.check_register(email)
        if check == True:
            account = db.create_account(username,email,password)
            if account == True:
                return redirect(url_for("user_module.login"))
            else:
                error = "Create Account Fail!"
        else:
            error = "Email Does Exist!"
    return render_template("Pages/register.html",error= error)

@user_module.route("/logout")
def logout():
    session['user_id'] = []
    session['role']=[]
    return redirect(url_for("index_module.index"))