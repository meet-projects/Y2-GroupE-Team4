from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
import random

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {
  "apiKey": "AIzaSyCQzrGhi1JdpqDhL_GfyXEfX52MbZkwKis",
  "authDomain": "isha-9977d.firebaseapp.com",
  "databaseURL": "https://isha-9977d-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "isha-9977d",
  "storageBucket": "isha-9977d.appspot.com",
  "messagingSenderId": "1032310546572",
  "appId": "1:1032310546572:web:34a33ede76ea79ec865ba9",
  "measurementId": "G-YZ4HRFXQ9R" 
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'







# @app.route('/donate', methods=['GET', 'POST'])
# def donate():
#     error = ""
#     donations = db.child("Donations").get().val()
#     if request.method == 'POST':
#         #try:
#             #need to add name attributes for each one & a donation display (in html) 
#         email = request.form['email'].lower()
#         name = request.form['name']
#         amount = request.form['amount']
#         donation = {"email": email, "name": name, "amount": amount}
#         db.child("Donations").push(donation)
#         donations = db.child("Donations").get().val()
#         return render_template("donate.html", donations = donations)

#        # except:
#             #error = "couldn't place donation, try again please"
#             #return render_template("donate.html", donations=donations, e=error)
#     else:
#         return render_template("donate.html",donations = donations)
#Route for signing up
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error=""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            print("trying")
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            UID = login_session['user']['localId']
            user = {"username":request.form['username'],"bio":request.form['bio']}
            db.child("Users").child(UID).set(user)
            print("added")
            return redirect(url_for('story'))
        except:
            error = "signup failed, please try again"
    return render_template("login.html",n=error)


#Route for signing in
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error=""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('story'))
        except:
            error = "sign in failed, please try again"
    return render_template("login.html",m=error)

#Route for moving to the login page (not the actual signing in)
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/story')
def story():
    return render_template("story.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/', methods=["GET","POST"])
def home():
    donations = db.child("Donations").get().val()
    if request.method == 'POST':
        try:
            projects = ["Community building project", "Women without status", "women and disabilities", "The Gun on the kitchen table", "Research center", "Young women project"]
            email = request.form['email'].lower()
            name = request.form['name']
            amount = request.form['amount']

            project = random.choice(projects)
            print(project)
            donation = {"email": email, "name": name, "amount": amount, "project": project}
            print(donation)
            db.child("Donations").push(donation)
            print('supossedly added donation?')
            donations = db.child("Donations").get().val()
            return redirect(url_for('donations'))
        except Exception as e:
            print(e)        
    return render_template("index2.html",donations = donations)
    


@app.route('/donations')
def donations():
    donations = db.child("Donations").get().val()
    return render_template("donations.html", donations = donations)





#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)