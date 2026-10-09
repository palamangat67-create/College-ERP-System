from django.contrib import admin
from myapp.models import Signup,Student,Faculty

# Register your models here.
admin.site.register(Signup)
admin.site.register(Student)
admin.site.register(Faculty)