from django.urls import path
from . import views

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),

    # Student manual attendance views (QR redirects here)
    path("student/", views.add_manually, name="add_manually"),
    path("student/submit", views.add_manually_post, name="add_manually_post"),
    path("student/submitted", views.submitted, name="submitted"),

    # Export and API
    path("export_excel", views.export_excel, name="export_excel"),
    path("api/present_students", views.get_present_students, name="get_present_students"),
]
