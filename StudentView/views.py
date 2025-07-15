from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.db import IntegrityError
from FacultyView.models import Student, Attendance

# Student view for manual attendance
def add_manually(request):
    students = Student.objects.all().order_by("s_roll")
    return render(request, "StudentView/StudentViewIndex.html", {
        "students": students,
    })

# Student attendance POST handler
def add_manually_post(request):
    if request.method == "POST":
        student_roll = request.POST.get("student-name")

        try:
            student = Student.objects.get(s_roll=student_roll)

            # Check if already marked
            if Attendance.objects.filter(student=student, date=now().date()).exists():
                return render(request, "StudentView/already_marked.html", {
                    "roll": student_roll,
                    "error": "Attendance already marked for today."
                })

            Attendance.objects.create(student=student)
            return redirect("submitted")

        except Student.DoesNotExist:
            return render(request, "StudentView/already_marked.html", {
                "roll": student_roll,
                "error": "Student not found!"
            })

    return redirect("add_manually")

# Confirmation page
def submitted(request):
    return render(request, "StudentView/Submitted.html")
