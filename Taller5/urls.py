"""Taller5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import *
import core.views as core_views

router = routers.DefaultRouter()
router.register(r'books', LibroViewSet)
router.register(r'authors', AutorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('books', core_views.list_books, name="list_books"),
    path('books/<int:pk>', core_views.book_detail, name="book_detail"),
    path('authors', core_views.list_authors, name="list_authors"),
    path('authors/<int:pk>', core_views.author_detail, name="author_detail"),
    path('profile', core_views.user_profile, name="profile"),
    path('books/<int:pk>/calificar', calificar, name="calificar")
]
