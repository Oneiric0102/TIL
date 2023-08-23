from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.login_views, name="login"),
    path("main/", views.login_success, name="main"),
    path("article", views.article_list, name="article_list"),
    path("create/", views.article_create, name="article_create"),
    path("logout/", views.logout_views, name="logout"),
    path("signup/", views.signup_views, name="signup"),
]
