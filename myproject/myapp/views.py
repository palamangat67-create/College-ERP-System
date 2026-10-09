
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from myapp.models import Signup
from .models import Student, Attendance,Result
from django.db import models
from .models import Faculty
from django.db.models import Count, Q
from django.contrib import messages
from functools import wraps

def login_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.session.get("user_id"):
            return redirect("login")
        return view(request, *args, **kwargs)
    return wrapper

def signup(request):

    if request.session.get("user_id"):
        return redirect("dashboard")

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if password != confirm_password:
            return render(request, "signup.html", {
                "msg": "Passwords do not match"
            })

        # Check if email already exists
        if Signup.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "msg": "Email already exists"
            })

        user = Signup.objects.create(
            fullname=fullname,
            email=email,
            uname=username,
            password=make_password(password),
            role=role
        )

        request.session["user_id"]=user.id
        request.session["username"]=user.uname
        messages.success(request, "Signed up successfully")
        return redirect("dashboard")

    return render(request, "signup.html")

def Login(req):
     if req.session.get("user_id"):
          return redirect("dashboard")

     if req.method=="POST":
          email=req.POST.get("email")
          password=req.POST.get("password")

          try:
           user=Signup.objects.get(email=email)
           if check_password(password,user.password):
                req.session["user_id"]=user.id
                req.session["username"]=user.uname
                messages.success(req, "Signed in successfully")
                return redirect("dashboard")
           else:
                return render(req,'login.html',{'msg':"invalid password"})
          except Signup.DoesNotExist:
             return render(req,'login.html',{'msg':"user does not exist"})

     return render(req,'login.html')

def Logout(req):
     req.session.flush()
     messages.success(req, "Logged out successfully")
     return redirect("login")


@login_required
def dashboard(req):
    return render(req,'dashboard.html')

@login_required
def add_student(request):
    if request.method == "POST":

        photo = request.FILES.get("photo")

        student_name = request.POST.get("student_name")
        roll_no = request.POST.get("roll_no")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        course = request.POST.get("course")
        semester = request.POST.get("semester")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        blood_group = request.POST.get("blood_group")
        transport = request.POST.get("transport")
        hostel = request.POST.get("hostel")
        address = request.POST.get("address")

        Student.objects.create(
            photo=photo,
            student_name=student_name,
            roll_no=roll_no,
            father_name=father_name,
            mother_name=mother_name,
            course=course,
            semester=semester,
            gender=gender,
            dob=dob,
            email=email,
            mobile=mobile,
            blood_group=blood_group,
            transport=transport,
            hostel=hostel,
            address=address,
        )

        return redirect("AddStudent")      # Change according to your URL name

    return render(request, "student/AddStudent.html")

@login_required
def add_faculty(req):

    if req.method == "POST":

        photo = req.FILES.get("photo")
        faculty_name = req.POST.get("faculty_name")
        employee_id = req.POST.get("employee_id")
        department = req.POST.get("department")
        designation = req.POST.get("designation")
        gender = req.POST.get("gender")
        dob = req.POST.get("dob")
        qualification = req.POST.get("qualification")
        experience = req.POST.get("experience")
        email = req.POST.get("email")
        mobile = req.POST.get("mobile")
        address = req.POST.get("address")

        Faculty.objects.create(
            photo=photo,
            faculty_name=faculty_name,
            employee_id=employee_id,
            department=department,
            designation=designation,
            gender=gender,
            dob=dob,
            qualification=qualification,
            experience=experience,
            email=email,
            mobile=mobile,
            address=address
        )

        return redirect("dashboard")

    return render(req, "faculty/Addfaculty.html")

@login_required
def view_student(request):
    students = Student.objects.all().order_by("roll_no")

    return render(request, "student/viewstudent.html", {
        "students": students
    })

@login_required
def view_faculty(request):
    faculties = Faculty.objects.all()

    return render(request, "faculty/viewfaculty.html", {
        "faculties": faculties
        })

@login_required
def student_profile(request, id):

    student = get_object_or_404(Student, id=id)

    return render(request,"student/studentprofile.html", {
        "student": student
    })

@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect("viewstudent")

@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        if request.FILES.get("photo"):
            student.photo = request.FILES.get("photo")

        student.student_name = request.POST.get("student_name")
        student.roll_no = request.POST.get("roll_no")
        student.father_name = request.POST.get("father_name")
        student.mother_name = request.POST.get("mother_name")
        student.course = request.POST.get("course")
        student.semester = request.POST.get("semester")
        student.gender = request.POST.get("gender")
        student.dob = request.POST.get("dob")
        student.email = request.POST.get("email")
        student.mobile = request.POST.get("mobile")
        student.blood_group = request.POST.get("blood_group")
        student.hostel = request.POST.get("hostel")
        student.transport = request.POST.get("transport")
        student.address = request.POST.get("address")

        student.save()

        return redirect("student_profile", id=student.id)

    return render(request," studen/teditstudent.html", {

        "student": student

    })

@login_required
def faculty_profile(request, id):

    faculty = get_object_or_404(Faculty, id=id)

    return render(request, "faculty/facultyprofile.html", {
        "faculty": faculty
    })

@login_required
def edit_faculty(request, id):

    faculty = get_object_or_404(Faculty, id=id)

    if request.method == "POST":

        if request.FILES.get("photo"):
            faculty.photo = request.FILES.get("photo")

        faculty.faculty_name = request.POST.get("faculty_name")
        faculty.employee_id = request.POST.get("employee_id")
        faculty.department = request.POST.get("department")
        faculty.designation = request.POST.get("designation")
        faculty.gender = request.POST.get("gender")
        faculty.dob = request.POST.get("dob")
        faculty.qualification = request.POST.get("qualification")
        faculty.experience = request.POST.get("experience")
        faculty.email = request.POST.get("email")
        faculty.mobile = request.POST.get("mobile")
        faculty.address = request.POST.get("address")
       
        faculty.save()

        return redirect("FacultyProfile", id=faculty.id)

    return render(request, "faculty/edit_faculty.html", {"faculty": faculty})


# Delete Faculty
@login_required
def delete_faculty(request, id):

    faculty = get_object_or_404(Faculty, id=id)

    faculty.delete()

    return redirect("viewfaculty")


@login_required
def mark_attendance(request):
    students = Student.objects.all()

    if request.method == "POST":
        date = request.POST.get("date")

        for student in students:
            status = request.POST.get(f"status_{student.id}")

            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={"status": status}
            )

        return redirect("markattendance")

    return render(request, "attendence/markattendance.html", {
        "students": students
    })


@login_required
def attendance_report(request):

    students = Student.objects.all()

    roll_no = request.GET.get("roll_no")
    course = request.GET.get("course")

    if roll_no:
        students = students.filter(roll_no__icontains=roll_no)

    if course:
        students = students.filter(course=course)

    attendance_report = []

    for student in students:

        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status="Present"
        ).count()

        absent = Attendance.objects.filter(
            student=student,
            status="Absent"
        ).count()

        if total > 0:
            percentage = round((present / total) * 100, 2)
        else:
            percentage = 0

        attendance_report.append({
            "roll_no": student.roll_no,
            "student_name": student.student_name,
            "total": total,
            "present": present,
            "absent": absent,
            "percentage": percentage,
        })

    courses = Student.objects.values_list(
        "course", flat=True
    ).distinct()

    return render(
        request,
        "attendence/attendancereport.html",
        {
            "attendance_report": attendance_report,
            "courses": courses,
        }
    )

@login_required
def add_result(request):

    students = Student.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student")
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        max_marks = request.POST.get("max_marks")
        marks_obtained = request.POST.get("marks_obtained")
        exam_type = request.POST.get("exam_type")

        student = Student.objects.get(id=student_id)

        Result.objects.create(
            student=student,
            semester=semester,
            subject=subject,
            max_marks=max_marks,
            marks_obtained=marks_obtained,
            exam_type=exam_type
        )

        return redirect("addresult")

    return render(request, "results/addresult.html", {
        "students": students
    })

@login_required
def view_result(request):

    results = Result.objects.select_related("student").all()

    for result in results:

        result.percentage = round(
            (result.marks_obtained / result.max_marks) * 100,
            2
        )

        if result.percentage >= 90:
            result.grade = "A+"
        elif result.percentage >= 80:
            result.grade = "A"
        elif result.percentage >= 70:
            result.grade = "B+"
        elif result.percentage >= 60:
            result.grade = "B"
        elif result.percentage >= 50:
            result.grade = "C"
        elif result.percentage >= 40:
            result.grade = "D"
        else:
            result.grade = "F"

    return render(request, "results/viewresult.html", {
        "results": results
    })