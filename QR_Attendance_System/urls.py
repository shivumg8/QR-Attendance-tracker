from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("FacultyView.urls")),        # Faculty homepage → /
    path("student/", include("StudentView.urls")),  # Student pages → /student/
]
