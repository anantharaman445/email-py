# tag = request.form["tag"]
# search = "%{}%".format(tag)
# posts = Post.query.filter(Post.tags.like(search)).all()


from flask import Flask
from flask import request,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ananth:ananth@localhost/ananth_test2'
db=SQLAlchemy(app)

# class Emails(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(100))
#     product=db.relationship('Product',backref='owner',lazy=True)

class Emails(db.Model):
    
    mail_id = db.Column(db.Text, primary_key=True)
    subject = db.Column(db.Text)
    from_add = db.Column(db.Text)
    epoch = db.Column(db.Float)

@app.route('/')
def home():
    return 'home'

@app.route('/post',methods=['POST','GET'])
def Productform():
    ob=Categ.query.all()
    if request.method=='POST':
        owner=request.form['ca']
        user = Categ.query.filter_by(name=owner).first()

        user=Product(pname=request.form['pname'],price=request.form['price'],owner=user)
        db.session.add(user)
        db.session.commit()

        return 'submit'

    return render_template('product.html',ob=ob)



@app.route('/categ',methods=['POST','GET'])
def Categoryform():
    if request.method=='POST':
        user=Categ(name=request.form['cname'])
        db.session.add(user)
        db.session.commit()

        return 'submit'

    return render_template('categ.html')


if __name__ == '__main__':
   app.run(debug=True)
   db.create_all()