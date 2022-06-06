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

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key = True, verbose_name = "Id tipo")
    nombreTipo = models.CharField(max_length = 10, verbose_name = "Admin Cliente", null = False, blank = False)
    
    def __str__(self):
        return self.nombreTipo


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name = "Id usuarios")
    nombre = models.CharField(max_length = 15, verbose_name = "Nombre Cliente", blank = False, null = False)
    apellido = models.CharField(max_length = 15, verbose_name = "Apellido Cliente", blank = False, null = False)
    clave = models.CharField(max_length = 15, verbose_name = "Contraseña", blank = False, null = False)
    correo = models.CharField(max_length = 15, verbose_name = "Correo", blank = False, null = False)
    idTipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)


    def __str__(self):
        return self.rut

class Region(models.Model):
    idRegion = models.AutoField(primary_key = True, verbose_name = "Id comuna")
    nregion = models.CharField(max_length = 30, verbose_name = "Nombre region", blank = False, null = False)

    def __str__(self):
        return self.nregion


class Comuna(models.Model):
    idComuna = models.AutoField(primary_key = True, verbose_name = "Id comuna")
    ncomuna = models.CharField(max_length = 30, verbose_name = "Nombre comuna", blank = False, null = False)
    idRegion = models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.ncomuna

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key = True, verbose_name="id Direccion")
    calle = models.CharField(max_length = 30, verbose_name = "Calle", blank = False, null = False)
    observacion = models.CharField(max_length = 40, verbose_name="Observacion si es Casa dpto etc", blank = True, null = True)
    idComuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.calle