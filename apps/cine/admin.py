from django.contrib import admin
from .models import Local, Pelicula, Sala, Funcion, Actor, Usuario, Venta 
# Register your models here.

admin.site.register(Local)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Funcion)
admin.site.register(Actor)
admin.site.register(Usuario)
admin.site.register(Venta)