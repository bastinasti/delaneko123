from django.db import models


# Create your models here.
class TipoProducto(models.Model):
    idTipProducto = models.AutoField(primary_key = True, verbose_name = "ID tipo producto")
    nomTipo = models.CharField(max_length = 15, verbose_name = "Gato Perro Exotico", blank = False, null = False)

    def __str__(self):
        return self.nomTipo


class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True, verbose_name = "La primary key de productos")
    nomProducto = models.CharField(max_length = 50, verbose_name = "Nombre del producto", blank = False, null = False)
    valor = models.IntegerField(verbose_name = "Valor producto")
    descripcion = models.CharField(max_length = 300, verbose_name = "Descripción del producto", blank = False, null = False)
    stock = models.IntegerField(verbose_name = "Cantidad de productos", blank = False, null = True)
    imgProducto = models.ImageField(upload_to = "productos")
    idTipProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomProducto

class TipoUser(models.Model):
    idtipo_user = models.AutoField(primary_key = True, verbose_name = "Id tipo")
    nomb_tipo = models.CharField(max_length = 10, verbose_name = "Admin Cliente", null = False, blank = False,)
    
    def __str__(self):
        return self.nomb_tipo


class Usuario(models.Model):
    rut = models.CharField(max_length = 10, primary_key = True, verbose_name = "Rut usuarios", null = True)
    username = models.CharField(max_length = 10, verbose_name = "Nombre de usuario", blank = True, null = True)
    clave = models.CharField(max_length = 15, verbose_name = "Contraseña", blank = False, null = False)
    nombre = models.CharField(max_length = 15, verbose_name = "Nombre Cliente", blank = False, null = False)
    apellido = models.CharField(max_length = 15, verbose_name = "Apellido Cliente", blank = False, null = False)
    correo = models.CharField(max_length = 15, verbose_name = "Correo", blank = False, null = False)
    telefono = models.CharField(max_length = 9, verbose_name = "Telefono Agregar el 9", blank = False, null = False)
    idtipo_user = models.ForeignKey(TipoUser, on_delete=models.CASCADE , null = True)


    def __str__(self):
        return self.rut