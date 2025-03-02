from flask import Flask, render_template
import os

def idx():
    return render_template("noimgvid.html")

def posts():
    return render_template("posts.html")

def login():
    return render_template("login.html")

def fun():
    return render_template("fun.html")

app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())

app.add_url_rule("/", "idx", idx)
app.add_url_rule("/posts", "posts", posts)
app.add_url_rule("/login", "login", login)
app.add_url_rule("/fun", "fun", fun)

app.run()
