from django.urls import path
from .import views
urlpatterns = [
    path('',views.Login,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.Logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('addStudent',views.add_student,name="AddStudent"),
    path('addfaculty', views.add_faculty, name="Addfaculty"),
    path('viewStudent',views.view_student, name="viewstudent"),
    path('viewfaculty', views.view_faculty, name="viewfaculty"),
    path('studentprofile/<int:id>/',views.student_profile,name="student_profile"),
    path("editStudent/<int:id>/", views.edit_student, name="EditStudent"),
    path("deleteStudent/<int:id>/", views.delete_student, name="DeleteStudent"),
    path("facultyProfile/<int:id>/",views.faculty_profile, name="FacultyProfile"),
    path("editFaculty/<int:id>/", views.edit_faculty, name="EditFaculty"),
    path("deleteFaculty/<int:id>/", views.delete_faculty, name="DeleteFaculty"),
    path('markattendance',views.mark_attendance,name="markattendance"),
    path('attendance-report',views.attendance_report,name="attendancereport"),
    path('addresult',views.add_result,name="addresult"),
    path('view-result',views.view_result,name="viewresult"),
]

