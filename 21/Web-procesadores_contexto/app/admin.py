from django.contrib import admin

# Register your models here.
from app import models

admin.site.register(models.Autor)
admin.site.register(models.editorial)
admin.site.register(models.libro)
admin.site.register(models.detalle_libro)
admin.site.register(models.disponibilidad_libro)
admin.site.register(models.modelo_extendido)