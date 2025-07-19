# Django Lab 2 – Course & Student Registration

## Objective
Build a simple Django application to manage course and student registrations.

---

## Requirements

### Models

1. **Course**
   - `name`: CharField
   - `description`: TextField

2. **Student**
   - `name`: CharField
   - `email`: EmailField
   - `course`: ForeignKey to Course

---

## Steps to Build

### 1. Create Models

In `models.py` of your app:

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

### 2. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 3. Admin Customization

In `admin.py`:

```python
from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course')
    search_fields = ('name', 'email')
```

---

### 4. Create Student Registration Form

In `forms.py`:

```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
```

---

### 5. Create Views

In `views.py`:

```python
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Course, Student

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return render(request, 'success.html', {'student': student})
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})
```

---

### 6. Configure URLs

In your app’s `urls.py`:

```python
from django.urls import path
from .views import register_student

urlpatterns = [
    path('register/', register_student, name='register_student'),
]
```

In the project’s main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')),
]
```

---

### 7. Templates

#### `register.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Register Student</title>
</head>
<body>
    <h1>Register New Student</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

#### `success.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h2>Registration Successful</h2>
    <p>Name: {{ student.name }}</p>
    <p>Email: {{ student.email }}</p>
    <p>Course: {{ student.course.name }}</p>
</body>
</html>
```

---

## Run the Server

```bash
python manage.py runserver
```

Then go to `http://127.0.0.1:8000/register/` in your browser.

---

## Admin Access

Create superuser:

```bash
python manage.py createsuperuser
```

Login at `http://127.0.0.1:8000/admin/` to manage courses and students.

---

## Notes

- Be sure to add your app to `INSTALLED_APPS` in `settings.py`.
- Run `python manage.py collectstatic` if needed for production use.