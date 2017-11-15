from flask import render_template, request, session, redirect, url_for, flash
from app import app
#from user import User
import user

#from shoppinglist import shoppinglists, Shoppinglist
import shoppinglist

user_details = user.User()
userlist= shoppinglist.Shoppinglist()
items = userlist.items_dict
#items = shoppinglist.items_dict
slists = shoppinglist.shoppinglists

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
        session['owner'] = request.form['email']
        password = request.form['password']
        details = user_details.login(email, password)
    
        if details == 5: #Login successfull
            session['email'] = request.form['email']
            return redirect(url_for('view', items_dict = items, lists = userlist.items_dict))
            
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
        count = 0

        if me_list == 8:
            return render_template("add-item-details.html", title = title, count = count)

        if me_list == 10:
            msg = "List already exists"
            return render_template("create-shopping-list.html", messages = msg)

    return render_template('create-shopping-list.html')

@app.route('/add<title>', methods=['GET', 'POST'])
def add(title):
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        budget = request.form['budget']
        owner = session['email']
        title = request.form['title']
        items_dict = userlist.add(title, item_name, quantity, budget)

        if items_dict == 9:
            return render_template("view-shopping-list.html", items_dict = items, lists = userlist.items_dict)
        else:
            print(items_dict)
    return render_template('add-item-details.html', title = title)

@app.route('/delete/<title>')
def delete_list(title):
    if request.method == 'GET':
        for list_name in userlist.items_dict.keys():
            if list_name == title:
                #shoppinglist.Shoppinglist.pop(list_name)
                userlist.items_dict.pop(list_name)
                return render_template("view-shopping-list.html", items_dict = items, lists = userlist.items_dict)
                
@app.route('/delete_item/<itemname>')
def delete_item(itemname):
    if request.method == 'GET':
        for title in userlist.items_dict.keys():
            for item in userlist.items_dict[title].keys():
                if item == itemname:
                    userlist.items_dict[title].pop(item)
                    return redirect(url_for('view'))
                continue
    return render_template("view-shopping-list.html")

@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'GET':
        pass

    return render_template("view-shopping-list.html", items_dict = items, lists = shoppinglist.shoppinglists)

@app.route('/logout')
def logout():
    if request.method == 'GET':
        if 'email' not in session:
            return redirect(url_for('login'))
        else:
            session.pop('owner', None)
            return render_template("index.html")