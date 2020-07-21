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

class TrainerTable(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    Akshit = db.Column(db.Float)
    SaiKrishna = db.Column(db.Float)
    Arun = db.Column(db.Float)
    Amogh = db.Column(db.Float)
    Abhishek = db.Column(db.Float)

@app.route('/')
def home():
    return render_template("indexpage.html")

@app.route('/feedback/',methods=['GET','POST'])
def feedback_form():
    if request.method == 'POST':
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
        score=0
        score=find_score(score,o_rate)
        score=find_score(score,h_on)
        score=find_score(score,explanation)
        score=find_score(score,doubt)
        if pace=="Just Perfect":
            score=score+1
        else:
            score=score+0.33
        data1 = TrainerTable.query.all()
        if trainer=="Akshit":
            if data1[0].Akshit == 0.0:
                data1[0].Akshit = score
            else:
                data1[0].Akshit = (data1[0].Akshit + score)/2.0
        if trainer=="SaiKrishna":
            if data1[0].SaiKrishna == 0.0:
                data1[0].SaiKrishna = score
            else:
                data1[0].SaiKrishna = (data1[0].SaiKrishna + score)/2.0
        if trainer=="Arun":
            if data1[0].Arun == 0.0:
                data1[0].Arun = score
            else:
                data1[0].Arun = (data1[0].Arun + score)/2.0
        if trainer=="Abhishek":
            if data1[0].Abhishek == 0.0:
                data1[0].Abhishek = score
            else:
                data1[0].Abhishek = (data1[0].Abhishek + score)/2.0
        if trainer=="Amogh":
            if data1[0].Amogh == 0.0:
                data1[0].Amogh = score
            else:
                data1[0].Amogh = (data1[0].Amogh + score)/2.0

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

def find_score(s,item):
    if item=='1' or item=='2':
        s=s+0.33
    elif item=='3':
        s=s+0.66
    else:
        s=s+1
    return s

@app.route('/Akshit/',methods=['GET','POST'])
def Akshit():
    data = TrainerTable.query.all()
    return render_template("Akshit1.html",data=data)

@app.route('/SaiKrishna/',methods=['GET','POST'])
def SaiKrishna():
    data = TrainerTable.query.all()
    return render_template("SaiKrishna.html",data=data)

@app.route('/Arun/',methods=['GET','POST'])
def Arun():
    data = TrainerTable.query.all()
    return render_template("Arun.html",data=data)

@app.route('/Abhishek/',methods=['GET','POST'])
def Abhishek():
    data = TrainerTable.query.all()
    return render_template("Abhishek.html",data=data)

@app.route('/Amogh/',methods=['GET','POST'])
def Amogh():
    data = TrainerTable.query.all()
    return render_template("Amogh.html",data=data)


if __name__=="__main__":
    db.create_all()
    app.run(port=8080,debug=True)
