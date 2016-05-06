from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "dontaskdonttell"
mysql = MySQLConnector(app, 'email_validation')

@app.route('/')
def index():

    return render_template('main.html')

@app.route('/addemail', methods = ['POST'])
def addemail():
	error_count = 0
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is not valid")
		error_count = 1
	if error_count > 0:
		return redirect('/')
	else:
		session['email'] = request.form['email']
		query = "INSERT INTO users (email, created_at) VALUES (:email, NOW())"
		data = {
			'email': request.form['email']
		   }

		mysql.query_db(query, data)
		return redirect('/success')

@app.route('/success')
def success():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	return render_template('success.html', all_users= users)

@app.route('/delete/<users_id>')
def delete(users_id):
	query = "DELETE FROM users WHERE id = :id"
	user = {'id' : users_id}
	mysql.query_db(query, user)
	return redirect('/success')

app.run(debug=True)