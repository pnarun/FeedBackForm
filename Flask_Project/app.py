from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask import session
from flask import flash
from flask_sqlalchemy import SQLAlchemy
import yaml
import os
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

'''db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
app.config['SECRET_KEY'] = os.urandom(20)'''

# Create table if not exist
class CreateTable(db.Model):
    __tablename__ = 'feedback_table'
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(30))
    USN = db.Column(db.String(30))
    Phn_no = db.Column(db.String(30))
    Email = db.Column(db.String(30))
    College = db.Column(db.String(30))
    Trainer = db.Column(db.String(30))
    Course = db.Column(db.String(30))
    Over_all_rating = db.Column(db.Integer)
    Hands_on = db.Column(db.Integer)
    Pace = db.Column(db.Integer)
    Explaination = db.Column(db.Integer)
    Doubt_clearing = db.Column(db.Integer)
    Suggestion = db.Column(db.String(100))

'''# Add the route to the Index page of the App
@app.route('/viewall/')
def index():
    cur =  mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM feedback_table")
    if (result_value > 0):
        data = cur.fetchall()
        return render_template('index.html', data=data)

@app.route('/feedback/', methods = ['GET'])
def newuser():
    if request.method == 'GET':
        form = request.form
        name =  form['name']
        password = form['age']
        cur =  mysql.connection.cursor()
        cur.execute("INSERT INTO new_users(name, password) VALUES(%s, %s)",(name, password))
        mysql.connection.commit()
        flash('Database inserted successfully')
    return render_template('newuser.html')'''

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)