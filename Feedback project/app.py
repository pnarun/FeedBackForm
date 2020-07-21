from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import redirect,request
from flask import url_for
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/flask_project'
db=SQLAlchemy(app)
class CreateTable(db.Model):
    __tablename__="feedback_table"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    usn=db.Column(db.String(20))
    phn_no=db.Column(db.String(20))
    email=db.Column(db.String(20))
    college=db.Column(db.String(20))
    trainer=db.Column(db.String(20))
    course=db.Column(db.String(20))
    overall_rate=db.Column(db.Integer)
    hands_on=db.Column(db.Integer)
    pace=db.Column(db.String(20))
    explanation=db.Column(db.Integer)
    doubt_clearing=db.Column(db.Integer)
    suggestions=db.Column(db.String(100))

@app.route('/')
def home():
    return render_template("indexpage.html")

@app.route('/feedback/',methods=['GET','POST'])
def feedback_form():
    if request.method=="POST":
        form = request.form
        name =  form['name']
        usn = form['usn']
        phone = form['phn']
        mail = form['mail']
        college = form['clgname']
        trainer = form['Trainee']
        course = form['rad']
        o_rate = form['rad1']
        h_on = form['rad2']
        pace = form['rad3']
        explanation = form['rad4']
        doubt = form['rad5']
        tarea = form['tarea']
        insert=CreateTable(name=name,usn=usn,phn_no=phone,email=mail,college=college,trainer=trainer,course=course,overall_rate=o_rate,hands_on=h_on,pace=pace,explanation=explanation,doubt_clearing=doubt,suggestions=tarea)
        save=db.session
        try:
            save.add(insert)
            save.commit()
            print("Successfully Entered feedback into Database")
            return redirect(url_for('thankyou'))
        except Exception as e:
            save.rollback()
            save.flush()
            print("Error in entering data into Database")
            print(e)
    return render_template("feedback.html")

@app.route('/thankyou/')
def thankyou():
    return render_template("thankyou.html")

@app.route('/viewall/',methods=['GET'])
def viewall():
    data = CreateTable.query.all()
    return render_template("viewall.html",data=data)

if __name__=="__main__":
    db.create_all()
    app.run(port=8080,debug=True)
