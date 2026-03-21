from flask import *   

from models import *
from db import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

student_bp = Blueprint("student", __name__)

@student_bp.route("/student-register", methods=["GET", "POST"])
def student_register():
  print("Route Hit student register")

  if request.method == "POST":
    print("POST request received")

    form_stu_name=request.form.get("stu_name")
    form_stu_age=request.form.get("stu_age")
    form_stu_email=request.form.get("stu_email")
    form_stu_phone=request.form.get("stu_phone")
    form_stu_address=request.form.get("stu_address")
    form_stu_password=request.form.get("stu_password")

    hashed_password = bcrypt.generate_password_hash(form_stu_password).decode("utf-8")


    try:
      stu_data = Student(
      stu_name=form_stu_name,
      stu_age=form_stu_age,
      stu_email=form_stu_email,
      stu_phone=form_stu_phone,
      stu_address=form_stu_address,
      stu_password = hashed_password,
      role = "student"
    )
      db.session.add(stu_data)
      db.session.commit()
      return redirect(url_for("student.all_students_data"))
    
    except Exception as e:
      return str(e)
    
  else:
    return render_template("students/register-student.html")
  

# All Students
@student_bp.route("/all-student", methods=["GET"])
def all_students_data():
    get_students = Student.query.all()   # select * from student
    print(type(get_students))
    return render_template("students/all_students.html", students = get_students)


#  One Student
@student_bp.route("/student-details/<int:id>")
def students_details(id):
    get_stu = Student.query.get(id)
    print(get_stu)
    return render_template("students/student-details.html", student = get_stu)

# Delete
@student_bp.route("/delete-student/<int:id>")
def delete_student(id):

    student = Student.query.get_or_404(id)

    if student:
        db.session.delete(student)
        db.session.commit()

    return redirect(url_for('student.all_students_data'))

# Update
@student_bp.route("/update-student/<int:id>", methods=["GET", "POST"])
def update_student(id):

    student = Student.query.get_or_404(id)

    if request.method == "POST":

        student.stu_name = request.form.get("stu_name")
        student.stu_age = request.form.get("stu_age")
        student.stu_email = request.form.get("stu_email")
        student.stu_phone = request.form.get("stu_phone")
        student.stu_address = request.form.get("stu_address")

        db.session.commit()

        return redirect(url_for('student.all_students_data'))

    return render_template("students/update-student.html", student=student)


@student_bp.route("/student-login", methods=["GET", "POST"])
def student_login():
  print("Route Hit student login")

  if request.method == "POST":
    print("POST request received")
    email = request.form.get("email")
    password = request.form.get("password")

    print(f"Email: {email}, Password: {password}")

    return f"Email: {email}, Password: {password}"

  return render_template("students/login-student.html")

