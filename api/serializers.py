from rest_framework import serializers
from core.models import *


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
