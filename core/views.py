from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def list_books(request):
    return render(request, "list_books.html")


@login_required
def user_profile(request):
    return render(request, "profile.html")


def book_detail(request):
    return render(request, "book.html")


def list_authors(request):
    return render(request, "list_authors.html")


def author_detail(request):
    return render(request, "author.html")
