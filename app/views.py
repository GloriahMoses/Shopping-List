from flask import render_template, request, session, redirect, url_for, flash
from app import app
import user
import shoppinglist

user_details = user.User()
userlist= shoppinglist.Shoppinglist()


app.secret_key = 'secret key'

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

        elif registered_user == 12:#Fill in all the fields
            msg = "Your password should be at least 6 characters long"
            return render_template('register.html', messages = msg)
        
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    """User login requests"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        details = user_details.login(email, password)
    
        if details == 5: #Login successfull
            session['email'] = request.form['email']
            return redirect(url_for('view', items_dict = shoppinglist.items_dict, lists = shoppinglist.shoppinglists))
            
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
        me_list = userlist.create(title,description,owner)

        if me_list == 8:
            return render_template("view-shopping-list.html", items_dict = shoppinglist.items_dict, lists = shoppinglist.shoppinglists)

        if me_list == 10:
            msg = "List already exists"
            return render_template("create-shopping-list.html", messages = msg)

    return render_template('create-shopping-list.html')

@app.route('/add/<titleadd>', methods=['GET', 'POST'])
def add(titleadd=None):
    if request.method =='POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        budget = request.form['budget']
        owner = session['email']
        results = userlist.add(title, item_name, quantity, budget)

        if results == 9:
            return render_template("view-shopping-list.html", items_dict = shoppinglist.items_dict, lists = shoppinglist.shoppinglists)
    return render_template('add-item-details.html', ttle=titleadd)

@app.route('/delete/<titledel>')
def delete_list(titledel=None):
    for list_name in shoppinglist.shoppinglists.keys():
        if list_name==titledel:
            shoppinglist.shoppinglists.pop(list_name)
            return redirect(url_for('view'))
                
@app.route('/delete_item/<itemdel>')
def delete_item(itemdel=None):
    for title in shoppinglist.items_dict.keys():
        for item in shoppinglist.items_dict[title].keys():
            if item == itemdel:
                shoppinglist.items_dict[title].pop(item)
                return render_template("view-shopping-list.html", items_dict = shoppinglist.items_dict, lists = shoppinglist.shoppinglists)

@app.route('/view')
def view():
    return render_template("view-shopping-list.html", items_dict = shoppinglist.items_dict, lists = shoppinglist.shoppinglists)

@app.route('/logout')
def logout():
    if request.method == 'GET':
        if 'email' not in session:
            return redirect(url_for('login'))
        else:
            session.pop('email')
            return render_template("index.html")
