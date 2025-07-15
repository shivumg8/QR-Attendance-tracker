from django.urls import path
from . import views

urlpatterns = [
    path("", views.faculty_view, name="faculty_view"),
    path("add_manually", views.add_manually, name="add_manually"),  # ✅ Important line
    path("add_manually_post", views.add_manually_post, name="add_manually_post"),
    path("submitted", views.submitted, name="submitted"),
    path("export_excel", views.export_excel, name="export_excel"),
    path("api/present_students", views.get_present_students, name="get_present_students"),
]
