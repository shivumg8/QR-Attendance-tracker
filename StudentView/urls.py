from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_manually, name="add_manually"),  # handles /student/
    path("submit", views.add_manually_post, name="add_manually_post"),  # handles /student/submit
    path("submitted", views.submitted, name="submitted"),  # handles /student/submitted
]
