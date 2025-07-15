from django.shortcuts import render
from FacultyView.models import Student, Attendance
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.db import IntegrityError

def add_manually_post(request):
    student_roll = request.POST.get("student-name")

    try:
        student = Student.objects.get(s_roll=student_roll)

        # If already marked, show error
        if Attendance.objects.filter(student=student, date=now().date()).exists():
            return render(request, "StudentView/already_marked.html", {
                "roll": student_roll,
                "error": "Attendance already marked for today."
            })

        Attendance.objects.create(student=student)
        return HttpResponseRedirect("/submitted")

    except Student.DoesNotExist:
        return render(request, "StudentView/already_marked.html", {
            "roll": student_roll,
            "error": "Student not found!"
        })

def submitted(request):
    return render(request, "StudentView/Submitted.html")
