from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/shorten_url/", views.shorten_url, name="shorten_url"),
    path("<str:short_url>/", views.redirect, name="redirect"),
]