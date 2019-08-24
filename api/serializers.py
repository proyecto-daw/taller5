from rest_framework import serializers
from core.models import *


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ("url", "nombre", "libros", "pk")


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    authors = AutorSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = ("url", "titulo", "isbn", "authors")
