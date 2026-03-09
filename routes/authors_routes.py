from flask import Blueprint, render_template, request

author_bp = Blueprint("author", __name__)

@author_bp.route("/author-register", methods=["GET","POST"])
def author_register():
    message = ""
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        message = f"Registered successfully: {full_name}"
    return render_template("author/author-register.html", message=message) 

@author_bp.route("/author-login", methods=["GET","POST"])
def author_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return f"Login Successful: {email}"
    return render_template("author/login-author.html") 