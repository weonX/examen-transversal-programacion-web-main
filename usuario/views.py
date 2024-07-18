from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UsuarioForm, PrecioForm, CategoríaForm, SupermercadoForm
from .models import Usuario, Precio, Categoría, Supermercado, Producto


def Pagina1(request):
    usuario = Usuario.objects.all()
    data = {'usuarios': usuario}
    return render(request, 'usuario/Pagina1.html', data)

def Pagina2(request):
    return render(request, 'usuario/Pagina2.html')

def Pagina3(request):
    return render(request, 'usuario/Pagina3.html')

def Pagina4(request):
    return render(request, 'usuario/Pagina4.html')

def Pagina5(request):
    return render(request, 'usuario/Pagina5.html')

def Pagina6(request):
    return render(request, 'usuario/Pagina6.html')

def registrar(request):
    Nombre_User = request.POST['nombre']
    Correo = request.POST['email']
    contraseña = request.POST['contraseña']

    usuarios = Usuario.objects.create(Nombre_User=Nombre_User, contraseña=contraseña, Correo=Correo)
    return redirect('/')

def producto1(request):
    ProductoListados = Producto.objects.all()
    return render(request, 'usuario/producto1.html', {"Producto": ProductoListados})

def registrarproducto(request):
    if request.method == 'POST':
        ID_Producto = request.POST.get('txtNumero_Id')
        Nombre_Produc = request.POST.get('txtproducto')
        Descripción = request.POST.get('txtdescripcion')

        # Crea una instancia del modelo Producto
        Producto.objects.create(
            ID_Producto=ID_Producto,
            Nombre_Produc=Nombre_Produc,
            Descripción=Descripción
        )
        
        # Vuelve a renderizar la página con la lista actualizada de productos
        ProductoListados = Producto.objects.all()
        return render(request, 'usuario/producto1.html', {"Producto": ProductoListados})
    else:
        # Renderiza el formulario si el método de solicitud no es POST
        ProductoListados = Producto.objects.all()
        return render(request, 'usuario/producto1.html', {"Producto": ProductoListados})
    




def editarproducto(request, ID_Producto):
    producto = get_object_or_404(Producto, ID_Producto=ID_Producto)
    return render(request, "usuario/editarproducto.html", {"producto": producto})

def actualizarproducto(request):
    ID_Producto = request.POST['ID_Producto']
    Nombre_Produc = request.POST['Nombre_Produc']
    Descripción = request.POST['Descripción']

    producto = get_object_or_404(Producto, ID_Producto=ID_Producto)
    producto.Nombre_Produc = Nombre_Produc
    producto.Descripción = Descripción
    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('producto1')

def eliminarproducto(request, ID_Producto):
    producto = get_object_or_404(Producto, ID_Producto=ID_Producto)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('producto1')

#----------------------------------------------------------------------------------------------

# Vistas CRUD para Usuario
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')

# Vistas CRUD para Precio
class PrecioListView(ListView):
    model = Precio
    template_name = 'precio/precio_list.html'
    context_object_name = 'precios'

class PrecioCreateView(CreateView):
    model = Precio
    form_class = PrecioForm
    template_name = 'precio/precio_form.html'
    success_url = reverse_lazy('precio_list')

class PrecioUpdateView(UpdateView):
    model = Precio
    form_class = PrecioForm
    template_name = 'precio/precio_form.html'
    success_url = reverse_lazy('precio_list')

class PrecioDeleteView(DeleteView):
    model = Precio
    template_name = 'precio/precio_confirm_delete.html'
    success_url = reverse_lazy('precio_list')

# Vistas CRUD para Categoría
class CategoriaListView(ListView):
    model = Categoría
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoría
    form_class = CategoríaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoría
    form_class = CategoríaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoría
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

# Vistas CRUD para Supermercado
class SupermercadoListView(ListView):
    model = Supermercado
    template_name = 'supermercado/supermercado_list.html'
    context_object_name = 'supermercados'

class SupermercadoCreateView(CreateView):
    model = Supermercado
    form_class = SupermercadoForm
    template_name = 'supermercado/supermercado_form.html'
    success_url = reverse_lazy('supermercado_list')

class SupermercadoUpdateView(UpdateView):
    model = Supermercado
    form_class = SupermercadoForm
    template_name = 'supermercado/supermercado_form.html'
    success_url = reverse_lazy('supermercado_list')

class SupermercadoDeleteView(DeleteView):
    model = Supermercado
    template_name = 'supermercado/supermercado_confirm_delete.html'
    success_url = reverse_lazy('supermercado_list')