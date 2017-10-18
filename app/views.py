from flask import render_template, request, session
from app import app
from user import User
from shoppinglist import Shoppinglist

user_details = User()
userlist= Shoppinglist()

app.secret_key = 'why would I tell you my secret key?'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/', methods=['GET','POST'])
def registration():
    """User registration requests"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        registered_user = user_details.registration(name, email, password, cpassword)

        if registered_user == 1: #successfully logged in
            return render_template('login.html')

        elif registered_user == 2:#Password dont match
            msg = "Passwords don't match, try again"
            return render_template('register.html', messages = msg)

        elif registered_user == 3:#Email already registred
            msg = "Email already registered, login"
            return render_template('login.html', messages = msg)

        elif registered_user == 4:#Fill in all the fields
            msg = "All fields are required, try again"
            return render_template('register.html', messages = msg)

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    """User login requests"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session['email'] = email
        details = user_details.login(email, password)
    
        if details == 5: #Login successfull
            return render_template('create-shopping-list.html')
            
        elif details == 6:#Wrong password
          msg = "Wrong email/password, try again"
          return render_template('login.html', messages = msg)

        elif details == 7: #Invalid Email
          msg = "Email not registered"
          return render_template('login.html', messages = msg)

    return render_template('login.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['shopping-list']
        description = request.form['list-description']
        owner = session['email']
        me_list =userlist.create(title,description,owner)
        if me_list == 8:
            return render_template("add-item-details.html")

    return render_template('create-shopping-list.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['item-name']
        price = request.form['item-name']
        quantity = request.form['Quantity']
        budget = request.form['estimated-budget']
        list_items = (name, price, quantity, budget)

        if list_items == 1:
           return render_template("view-shopping-list.html")
            
    return render_template("add-item-details.html")

@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template("view-shopping-list.html")
