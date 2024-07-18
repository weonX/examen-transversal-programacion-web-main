from django.urls import path
from .views import (
    Pagina1, Pagina2, Pagina3, Pagina4, Pagina5, Pagina6,
    registrar, producto1, registrarproducto, editarproducto, actualizarproducto, eliminarproducto,
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    PrecioListView, PrecioCreateView, PrecioUpdateView, PrecioDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    SupermercadoListView, SupermercadoCreateView, SupermercadoUpdateView, SupermercadoDeleteView,
)

urlpatterns = [
    path('', Pagina1, name='Pagina1'),
    path('registrar/', registrar, name='registrar'),
    path('Pagina2/', Pagina2, name='Pagina2'),
    path('Pagina3/', Pagina3, name='Pagina3'),
    path('Pagina4/', Pagina4, name='Pagina4'),
    path('Pagina5/', Pagina5, name='Pagina5'),
    path('Pagina6/', Pagina6, name='Pagina6'),
    path('producto1/', producto1, name='producto1'),
    path('registrarproducto/', registrarproducto, name='registrarproducto'),
    path('editarproducto/<int:ID_Producto>/', editarproducto, name='editarproducto'),
    path('actualizarproducto/', actualizarproducto, name='actualizarproducto'),
    path('eliminarproducto/<int:ID_Producto>/', eliminarproducto, name='eliminarproducto'),

    # URLs para Usuario
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/crear/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),

    # URLs para Precio
    path('precios/', PrecioListView.as_view(), name='precio_list'),
    path('precios/crear/', PrecioCreateView.as_view(), name='precio_create'),
    path('precios/<int:pk>/editar/', PrecioUpdateView.as_view(), name='precio_update'),
    path('precios/<int:pk>/eliminar/', PrecioDeleteView.as_view(), name='precio_delete'),

    # URLs para Categoría
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    # URLs para Supermercado
    path('supermercados/', SupermercadoListView.as_view(), name='supermercado_list'),
    path('supermercados/crear/', SupermercadoCreateView.as_view(), name='supermercado_create'),
    path('supermercados/<int:pk>/editar/', SupermercadoUpdateView.as_view(), name='supermercado_update'),
    path('supermercados/<int:pk>/eliminar/', SupermercadoDeleteView.as_view(), name='supermercado_delete'),
]
