from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import now
from django.utils.dateparse import parse_date
from django.views.decorators.http import require_GET
from django.conf import settings
from .models import Student, Attendance
from datetime import date
import qrcode
import openpyxl
import os
from django.db import IntegrityError

def qrgenerator():
    file_path = os.path.join("FacultyView", "static", "FacultyView", "qrcode.png")

    # Remove old QR
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Old QR code deleted.")

    # Use Render domain from settings
    base_url = getattr(settings, "QR_CODE_BASE_URL", "https://qr-attendance-tracker-ytvw.onrender.com")
    full_url = f"{base_url}/student/add_manually"

    print("QR_CODE_BASE_URL:", base_url)
    print("Full QR URL:", full_url)

    img = qrcode.make(full_url)
    img.save(file_path)
    print(f"New QR code generated at {file_path} pointing to {full_url}")

def faculty_view(request):
    if request.method == "POST":
        student_roll = request.POST.get("student_id")
        try:
            student = Student.objects.get(s_roll=student_roll)
            Attendance.objects.filter(student=student, date=now().date()).delete()
        except Student.DoesNotExist:
            pass
        return redirect("faculty_view")

    qrgenerator()
    students = Student.objects.filter(attendance__date=now().date()).distinct()
    return render(request, "FacultyView/FacultyViewIndex.html", {"students": students})

@require_GET
def export_excel(request):
    date_str = request.GET.get("date")
    date_obj = parse_date(date_str)
    if not date_obj:
        return HttpResponse("Invalid date", status=400)

    records = Attendance.objects.filter(date=date_obj).select_related("student")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Roll No", "First Name", "Last Name", "Branch", "Year", "Section", "Date"])

    for r in records:
        s = r.student
        ws.append([
            s.s_roll, s.s_fname, s.s_lname,
            s.s_branch.branch, s.s_year.year,
            s.s_section.section, r.date
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="Attendance_{date_str}.xlsx"'
    wb.save(response)
    return response

@require_GET
def get_present_students(request):
    today = date.today()
    attendances = Attendance.objects.filter(date=today).select_related("student")
    data = [
        {"roll": a.student.s_roll, "name": f"{a.student.s_fname} {a.student.s_lname}"}
        for a in attendances
    ]
    return JsonResponse({"students": data})

def add_manually(request):
    students = Student.objects.all().order_by("s_roll")
    return render(request, "StudentView/StudentViewIndex.html", {"students": students})

def add_manually_post(request):
    if request.method == "POST":
        student_roll = request.POST.get("student-name")
        try:
            student = Student.objects.get(s_roll=student_roll)
            Attendance.objects.create(student=student, date=now().date())
            return redirect("submitted")
        except Student.DoesNotExist:
            return render(request, "StudentView/already_marked.html", {
                "roll": student_roll,
                "error": "Student not found!"
            })
        except IntegrityError:
            return render(request, "StudentView/already_marked.html", {
                "roll": student_roll,
                "error": "Attendance already marked for today."
            })
    return redirect("add_manually")

def submitted(request):
    return render(request, "StudentView/Submitted.html")
