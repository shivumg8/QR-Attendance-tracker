from django.urls import path
from . import views

urlpatterns = [
    path("add_manually/", views.add_manually, name="add_manually"),
    path("add_manually_post/", views.add_manually_post, name="add_manually_post"),
    path("submitted/", views.submitted, name="submitted"),
]
