from flask import Flask, render_template, flash, redirect, url_for
from forms import Register, Login
import datetime
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "f30c2287636aacb63efb459dc492b223"


response = requests.get(url="https://api.npoint.io/d59a1dba2ea5c13cdb14")
data = response.json()
print(data)


today = datetime.datetime.now()
year = today.year


@app.route("/")
def go_home():
    return render_template("index.html", data=data, title='Home', year=year)


@app.route("/about")
def about():
    return render_template("about.html", title='About', year=year)


@app.route("/post/<int:num>")
def show_post(num):
    return render_template("post.html", title='Show more', year=year, data=data, num=num)


@app.route("/main")
def main():
    return render_template("main.html", year=year)


@app.route("/register",methods =['POST', 'GET'])
def register_now():
    form = Register()
    if form.validate_on_submit():
        flash("new user has been created","success")
        return redirect(url_for('about'))
    return render_template("register.html", title='Register', year=year, form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = Login()
    return render_template("login.html", title='Login', year=year, form=form)


if __name__ == '__main__':
    app.run(debug=True)
