from flask import render_template, request, url_for, redirect
from app import app
from user import User
details = User()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/', methods=['GET', 'POST'])

def registration():
	if request.method == 'POST' and request.method == 'GET':
		name = request.form.get['name']
		email = request.form.get['email']
		password = request.form.get['password']
		cpassword = request.form.get['cpassword']
		user_details = details.registration(email, name, password, cpassword)
		if user_details == 1:
			return render_template('login.html')
		
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    return render_template('login.html')