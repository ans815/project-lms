from flask import *
book_bp = Blueprint("book", __name__)

@book_bp.route("/book-register", methods=["GET", "POST"])
def book_register():
    if request.method == "POST":

        title = request.form.get("title")
        author = request.form.get("author")
        return f"Book Registered: {title} by {author}"

    return render_template("books/register-book.html")


@book_bp.route("/book-login", methods=["GET", "POST"])
def book_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return f"Login Successful: {email}"

    return render_template("books/login-book.html")