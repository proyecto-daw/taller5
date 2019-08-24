from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Libro)
admin.site.register(User)
admin.site.register(Autor)
admin.site.register(Rating)
