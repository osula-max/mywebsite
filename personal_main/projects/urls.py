from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cv/", views.cv, name="cv"),
    path("contact/", views.contact, name="contact"),
    path("works/", views.works, name="works"),
]