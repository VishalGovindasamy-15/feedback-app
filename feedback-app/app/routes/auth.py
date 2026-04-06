from flask import Blueprint, render_template, request
from db import db
from models import User

auth = Blueprint('auth', __name__)

# REGISTER → create user
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return "User registered successfully!"

    return render_template("register.html")


# LOGIN → check user
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return "Login successful!"
        else:
            return "Invalid credentials"

    return render_template("login.html")