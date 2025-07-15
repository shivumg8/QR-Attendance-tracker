# QR_Attendance_System/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FacultyView.urls")),
    path("student/", include("StudentView.urls")),  # ✅ Separate student views under /student/
]
