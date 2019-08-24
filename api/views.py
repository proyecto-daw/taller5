from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.serializers import LibroSerializer, AutorSerializer
from core.models import *


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAdminOrReadOnly]


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAdminOrReadOnly]


@login_required
def calificar(request, pk):
    if request.method == 'POST':
        request.user.ratings.create(libro=Libro.objects.get(pk=pk), rating=request.POST["rating"])
        return redirect('profile')
    return HttpResponse(status=405)  # HTTP Not Allowed
