from application import app
from flask import render_template, request, Response, redirect, flash, url_for, session
from application.forms import SignInForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        flash(f"Welcome, {username}! You've successfully logged in.", category="success")
        return redirect(url_for('home'))
    return render_template("index.html", form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    username = request.form.get('username')
    return render_template('home.html', username=username)





def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/shutdown")
def shutdown():
    shutdown_server()
    return "Server shutting down. Please close this window"
