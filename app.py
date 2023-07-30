from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

config = {
  "apiKey": "AIzaSyCQzrGhi1JdpqDhL_GfyXEfX52MbZkwKis",
  "authDomain": "isha-9977d.firebaseapp.com",
  "projectId": "isha-9977d",
  "storageBucket": "isha-9977d.appspot.com",
  "messagingSenderId": "1032310546572",
  "appId": "1:1032310546572:web:34a33ede76ea79ec865ba9",
  "measurementId": "G-YZ4HRFXQ9R"
  "databaseURL": "https://isha-9977d-default-rtdb.europe-west1.firebasedatabase.app/"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)