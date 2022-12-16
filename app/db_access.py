import psycopg2
from app import app


class DataAccountAccess:
    def __init__(self):
        self.cur = None
        self.conn = None

    def connect_db(self):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                host="localhost",
                database="Food_DB",
                user="postgres",
                password="admin123",
            )
            # create a cursor
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            print("Unable to connect %s" % str(e))
            return None

    def check_login(self,email,password):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'SELECT * FROM accounts Where email = %s and password = %s ',
                (email, password)
            )
            # display the PostgreSQL database server version
            account_info = self.cur.fetchall()
            if len(account_info) > 0:
                return True
            else:
                return False
        except Exception as e:
            print("Check Login error: "+str(e))
            return False

    def check_register(self,email):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'SELECT * FROM accounts Where email = %s',
                (email,)
            )
            # display the PostgreSQL database server version
            account_info = self.cur.fetchall()
            if len(account_info) > 0:
                return False
            else:
                return True
        except Exception as e:
            print("Check Register error: "+str(e))
            return False

    def create_account(self,username,email,password,role="user"):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'Insert Into accounts(username,email,password,role) Values(%s,%s,%s,%s)',
                (username,email,password,role)
            )
            self.conn.commit()
            self.cur.close()
            return True
        except Exception as e:
            print("Create Account error: "+str(e))
            return False

    def get_user_id(self,email):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'Select user_id from accounts Where email=%s',
                (email,)
            )
            user_id = self.cur.fetchone()
            return user_id
        except Exception as e:
            print("Create Account error: "+str(e))
            return None

    def get_role(self,email):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute(
                'Select role from accounts Where email=%s',
                (email,)
            )
            role = self.cur.fetchone()
            return role
        except Exception as e:
            print("Get role error: "+str(e))
            return None

class DataProductAccess:
    def __init__(self):
        self.cur = None
        self.conn = None

    def connect_db(self):
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(
                host="localhost",
                database="Food_DB",
                user="postgres",
                password="admin123",
            )
            # create a cursor
            cur = conn.cursor()
            return conn, cur
        except Exception as e:
            print("Unable to connect %s" % str(e))
            return None

    def get_product(self,limit_product,page=1):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            offset = (page-1)*limit_product
            self.cur.execute('Select * From products Limit %s Offset %s',(limit_product,offset,))
            list_product = self.cur.fetchall()
            return list_product
        except Exception as e:
            print("Get Product error: "+str(e))
            return None
    
    def get_singleproduct(self,product_name):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select * From products Where product_name=%s',(product_name,))
            single_product = self.cur.fetchone()
            return single_product
        except Exception as e:
            print("Get Product error: "+str(e))
            return None

    def get_product_by_chef(self,chef):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select * From products Where chef=%s',(chef,))
            list_product = self.cur.fetchall()
            return list_product
        except Exception as e:
            print("Get Product error: "+str(e))
            return None

    def insert_order(self,user_id,fullname,email,address,phone,order_date,delivery_date,order_number,product_list,total):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Insert Into cart (user_id,fullname,email,address,phone,order_date,delivery_date,order_number,product_list,total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(user_id,fullname,email,address,phone,order_date,delivery_date,order_number,product_list,total,))
            self.conn.commit()
            self.cur.close()
            return True
        except Exception as e:
            print("Insert order error: "+str(e))
            return False

    def insert_product(self,product_name,price,time_order,type_food,image,chef,story,story2,story3):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Insert Into products (product_name,price,time_order,type_food,image,chef,story,story2,story3) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(product_name,price,time_order,type_food,image,chef,story,story2,story3))
            self.conn.commit()
            self.cur.close()
            return True
        except Exception as e:
            print("Insert products error: "+str(e))
            return False

    def count_product(self):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select Count(*) From products')
            quantity = self.cur.fetchone()
            return quantity[0]
        except Exception as e:
            print("Insert order error: "+str(e))
            return None

    def get_product_by_table(self,table_id):
        try:
            if self.cur == None:
                self.conn, self.cur = self.connect_db()
            self.cur.execute('Select * From order_temp Where table_id=%s',(table_id,))
            list_product = self.cur.fetchall()
            return list_product
        except Exception as e:
            print("Get Order temp error: "+str(e))
            return None


    