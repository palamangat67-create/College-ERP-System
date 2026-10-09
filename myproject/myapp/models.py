from django.db import models

# Create your models here.
class Signup(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    uname = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.uname

class Student(models.Model):
    photo = models.ImageField(upload_to="students/", blank=True, null=True)

    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=30, unique=True)

    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    course = models.CharField(max_length=50)
    semester = models.CharField(max_length=30)

    gender = models.CharField(max_length=10)

    dob = models.DateField()

    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)

    blood_group = models.CharField(max_length=5)

    transport = models.CharField(max_length=10)
    hostel = models.CharField(max_length=10)

    address = models.TextField()

    def __str__(self):
        return self.student_name

class Faculty(models.Model):

    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
    faculty_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()

def __str__(self):
        return self.faculty_name    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10)

def __str__(self):
        return f"{self.student.student_name} - {self.status}"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    semester = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)

    max_marks = models.IntegerField(default=100)
    marks_obtained = models.IntegerField()

    exam_type = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_name} - {self.subject}"