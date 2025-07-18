from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Student

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course')
    search_fields = ('name', 'email')
    list_filter = ('course',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
