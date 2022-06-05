from django.contrib import admin
from .models import TipoProducto, Producto, TipoUsuario, Usuario, Region, Comuna, Direccion

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
