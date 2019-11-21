from django.urls import path

from .views import homepage_view, ListView, DetailView


urlpatterns = [
    path("", homepage_view, name="home"),
    path("articles/", ListView.as_view(), name="articles"),
    path("articles/<slug:slug>/", DetailView.as_view(), name="article_detail"),
]
