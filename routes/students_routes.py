# from flask import *
from flask import Blueprint, render_template, request, redirect, url_for
from models import Student
from db import db

student_bp = Blueprint("student", __name__)

# students register
@student_bp.route("/student-register", methods=["GET", "POST"])
def student_register():
    if request.method == "POST":
        form_stu_name = request.form.get("stu_name")
        form_stu_age = request.form.get("stu_age")
        form_stu_email = request.form.get("stu_email")
        form_stu_phone = request.form.get("stu_phone")
        form_stu_address = request.form.get("stu_address")
        form_stu_password = request.form.get("stu_password")
        
        try:
            stu_data = Student(
                stu_name=form_stu_name,
                stu_age=int(form_stu_age),
                stu_email=form_stu_email,
                stu_phone=form_stu_phone,
                stu_address=form_stu_address,
                stu_password=form_stu_password
            )

            db.session.add(stu_data) 
            db.session.commit()
        
            return redirect(url_for("student.all_students_data"))
        except Exception as e:
            return str(e)
    
    else:
        return render_template("students/register-student.html")


@student_bp.route("/all-students")
def all_students_data():
    get_students = Student.query.all()  # select * from students
    return render_template("students/all_students.html", students=get_students)


@student_bp.route("/student-details/<int:id>")
def students_details(id):
    get_stu = Student.query.get(id)
    return render_template("students/student-details.html", student=get_stu)