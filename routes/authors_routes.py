from flask import *

from models import *
from db import db

author_bp = Blueprint("author", __name__)

@author_bp.route("/author-register", methods=["GET","POST"])
def author_register():
    print("Route Hit author register")

    if request.method == "POST":
        print("POST request received")

        form_auth_name = request.form.get("auth_name")
        form_auth_age = request.form.get("auth_age")
        form_auth_email = request.form.get("auth_email")
        form_auth_phone = request.form.get("auth_phone")
        form_auth_address = request.form.get("auth_address")

        role = "author"

        try:
            auth_data = Author(
                auth_name=form_auth_name,
                auth_age=form_auth_age,
                auth_email=form_auth_email,
                auth_phone=form_auth_phone,
                auth_address=form_auth_address,
                role=role
            )

            db.session.add(auth_data)
            db.session.commit()

            return redirect(url_for("author.all_authors_data"))

        except Exception as e:
            return str(e)

    else:
        return render_template("authors/register-author.html")
  
@author_bp.route("/all-author")
def all_authors_data():

    get_author = Author.query.all()
    print(get_author)

    print(type(get_author))

    return render_template("authors/all_authors.html", authors = get_author
    )

@author_bp.route("/author-details/<int:id>")
def authors_details(id):
    get_auth = Author.query.get(id)
    print(get_auth)
    return render_template("authors/author-details.html", author = get_auth)


# Delete
@author_bp.route("/delete-author/<int:id>")
def delete_author(id):

    author = Author.query.get_or_404(id)

    if author:
        db.session.delete(author)
        db.session.commit()

    return redirect(url_for('author.all_authors_data'))


# Update
@author_bp.route("/update-author/<int:id>", methods=["GET", "POST"])
def update_author(id):

    author = Author.query.get_or_404(id)

    if request.method == "POST":

        author.auth_name = request.form.get("auth_name")
        author.auth_age = request.form.get("auth_age")
        author.auth_email = request.form.get("auth_email")
        author.auth_phone = request.form.get("auth_phone")
        author.auth_address = request.form.get("auth_address")

        db.session.commit()

        return redirect(url_for('author.all_authors_data'))

    return render_template("authors/update-author.html", author=author)


@author_bp.route("/author-login", methods=["GET","POST"])
def author_login():
  print("Route Hit author login")
  
  if request.method == "POST":
    print("POST request received")
    email = request.form.get("email")
    password = request.form.get("password")

    print(f"Email: {email}, Password: {password}")

    return f"Email: {email}, Password: {password}"
  
  return render_template("authors/login-author.html")

