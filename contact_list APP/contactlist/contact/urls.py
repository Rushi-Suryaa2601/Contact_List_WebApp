from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_contact/", views.add_contact, name="add_contact"),
    path("profile/<str:pk>", views.contactprofile, name="profile"),
    path("edit_contact/<str:pk>", views.edit_contact, name="edit_contact"),
    path("delete_contact/<str:pk>", views.delete_contact, name="delete_contact"),
]
