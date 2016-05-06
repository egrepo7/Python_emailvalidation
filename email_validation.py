from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
@app.route('/')
def index():
    return render_template('main.html')

# @app.route('/friends', methods=['POST'])
# def create():
#     # add a friend to the database!
#     return redirect('/')
app.run(debug=True)