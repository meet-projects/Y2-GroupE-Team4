from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

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



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        try:
            email = request.form['email'].lower()
            name = request.form['name']
            amount = request.form['amount']
            donation = {"email": email, "name": name, "amount": amount}
            db.child("Donations").push(donation)
            return render_template("donate.html")

        except:
            return render_template("donate.html")
    else:
        return render_template("donate.html")

















#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)