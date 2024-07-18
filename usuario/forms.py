from django import forms
from .models import Usuario, Precio, Categoría, Supermercado

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['ID_Usuario', 'Correo', 'contraseña', 'Nombre_User']

class PrecioForm(forms.ModelForm):
    class Meta:
        model = Precio
        fields = ['ID_Precio', 'Precio_Prod']

class CategoríaForm(forms.ModelForm):
    class Meta:
        model = Categoría
        fields = ['ID_Categoría', 'Nombre_Catego']

class SupermercadoForm(forms.ModelForm):
    class Meta:
        model = Supermercado
        fields = ['ID_Supermercado', 'Nombre_tienda', 'URL']