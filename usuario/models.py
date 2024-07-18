from django.db import models

class Producto(models.Model):
    ID_Producto = models.PositiveIntegerField(primary_key=True, unique=True, verbose_name='ID')
    Nombre_Produc = models.CharField(max_length=50, unique=True, verbose_name='Nombre Producto')
    Descripción = models.CharField(max_length=100, unique=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.ID_Producto, self.Nombre_Produc)

class Usuario(models.Model):
    ID_Usuario = models.PositiveIntegerField(primary_key=True, unique=True, verbose_name='ID')
    Correo = models.EmailField(unique=True, verbose_name='Correo Electronico')
    contraseña = models.CharField(max_length=50)
    Nombre_User = models.CharField(max_length=50, unique=True, verbose_name='Nombre de Usuario')
    Fechar_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.Correo, self.Nombre_User, self.ID_Usuario, self.Fechar_registro)

class Precio(models.Model):
    ID_Precio = models.AutoField(primary_key=True)
    Precio_Prod = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ID_Precio}: {self.Precio_Prod}"
    
class Categoría(models.Model):
    ID_Categoría = models.PositiveIntegerField(primary_key=True, unique=True, verbose_name='ID')
    Nombre_Catego = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.ID_Categoría, self.Nombre_Catego)

class Supermercado(models.Model):
    ID_Supermercado = models.PositiveIntegerField(primary_key=True, unique=True, verbose_name='ID')
    Nombre_tienda = models.CharField(max_length=50, unique=True)
    URL = models.CharField(max_length=50, unique=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.ID_Supermercado, self.Nombre_tienda)
