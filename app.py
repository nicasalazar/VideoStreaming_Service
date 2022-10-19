from crypt import methods
from flask import Flask, render_template
from flask import flash, request, redirect,session



app = Flask(__name__)
app.secret_key = 'SuperSecret'

user = {"username": "admin", "password": "password"}

@app.route("/", methods = ['POST', 'GET'])
def index():
    return render_template("login.html")


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('http://localhost:5001/upload')

        return "<h1>Wrong username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")

@app.route("/dashboard")
def dashboard(): 
    if('user' in session and session['user'] == user['username']):
        return '<h1>Video Dashboard</h1>'
    #here we are checking whether the user is logged in or not

    return '<h1>You are not logged in.</h1>'  #if the user is not in the session


if __name__ == '__main__':
    app.run(port=5000)