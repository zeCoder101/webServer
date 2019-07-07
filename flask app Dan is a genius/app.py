from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from user import User, get_id

app = Flask(__name__)
app.secret_key = 'kzbdofbnsjhbQHBEZJHFKKJJHSJHBS48641133158jjsejhbvbgggggggggg'
login_manager = LoginManager(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return get_id(user_id)


@app.route('/')
def hello_world():
	name = request.args.get('name', '')
	if current_user.is_authenticated:
		name = current_user.name
	return render_template("index.html", name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		user =  get_id(request.form.get('usr'))
		password = request.form.get('pwd')
		if user and password == user.password:
			login_user(user)
			return redirect('/secret')
	return render_template('login.html')


@app.route('/goodbye')
def goodbye():
	name = request.args.get('name', 'undefined')
	logout_user()
	return render_template("goodbye.html", name=name)


@app.route('/secret')
@login_required
def secret():
	return render_template('secret.html')	


@app.route('/goodbye/admin')
def goodbye_admin():
	name = request.args.get('name', '')
	if len(name) > 0:
		return 'goodbye ' + name
	return 'bye thx for controlling Me._.'


@app.route('/goodbye/<name>')
def goodbye_name(name):
	return 'goodbye ' + name 


@app.route('/menu')
def menu():
	return render_template('menupage.html')

@app.route('/party')
@login_required
def party():
	return render_template('party.html')

@app.route('/utility')
def utility():
	return render_template('utility.html')

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html')