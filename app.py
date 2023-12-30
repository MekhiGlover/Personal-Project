from flask import Flask, render_template, request,redirect
import math
import random
app = Flask(__name__)

Users = []



class User:
    def __init__(self,username,email,password):
        self.username = username,
        self.email = email,
        self.password = password
        self.user_id = math.ceil(random())





# CREATING ROUTES BETWEEN ALL PAGES

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/page2')
def second():
    return render_template('other.html')

@app.get('/page3')
def third():
    return render_template('p3.html')


# CREATING ROUTES TO LOG IN AND OUT 



@app.post('/signup/<string:username>/<string:email>/<string:password>')
def create(username,email,password):
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    newUser = User.__init__(username=username, email = email, password=password)
    Users.append(newUser)
    for person in Users:
        print(person)
    return redirect('/')