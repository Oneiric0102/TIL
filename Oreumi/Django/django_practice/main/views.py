from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Article


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    return render(request, "main/article_list.html", {"articles": articles})


def article_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        Article.objects.create(title=title, content=content)
        return redirect("article_list")

    return render(request, "main/article_create.html")


def login_views(request):
    return render(request, "main/login.html")


def login_success(request):
    username = request.user
    return render(request, "main/main.html", {"username": username})


def logout_views(request):
    logout(request)
    return redirect("login")


def signup_views(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article_list")
    else:
        form = UserCreationForm()
        return render(request, "main/signup.html", {"form": form})
