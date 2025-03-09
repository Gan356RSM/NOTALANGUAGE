from flask import Flask, render_template, request
import os

blog_posts = [
    {"pid":0,
     "title":"Skibidi",
     "content":"Skibidi Toilet is brainrot",
     "author":"Rocks Sigma"
    },
    {"pid":1,
     "title":"Sigma",
     "content":"Sigma Rizzler",
     "author":"dum as khang"
    }
]

def idx():
    return render_template("noimgvid.html")

def posts():
    return render_template("posts.html")

def login():
    return render_template("login.html")

def fun():
    return render_template("fun.html")

def nig():
    value = request.args.get("pid")
    if value == None:
        return render_template("nig.html", blog_posts=blog_posts)
    else:
        pid = int(value)
        for p in blog_posts:
            if p["pid"] == pid:
                return render_template("nickel.html",blog_data=p)
            
        return render_template("nig.html", blog_posts=blog_posts)

app = Flask(__name__, template_folder=os.getcwd(), static_folder=os.getcwd())

app.add_url_rule("/", "idx", idx)
app.add_url_rule("/posts", "posts", posts)
app.add_url_rule("/login", "login", login)
app.add_url_rule("/fun", "fun", fun)
app.add_url_rule("/nig", "nig", nig)

app.run()
