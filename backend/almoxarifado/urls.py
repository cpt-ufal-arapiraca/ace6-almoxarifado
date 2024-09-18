from django.urls import path
from almoxarifado.views.usuario_view import  (UserRegister, UserLogin, UserLogout, UserView,
                                              UserListView, ModuleListView, ModuleCreateView,
                                              ModuleDeleteView, ModuleUpdateView, AddModuleToUserView)
from almoxarifado.views.pedido_view import  (PedidoListView, PedidoCreateView, UserPedidoListView, 
                                             PedidoByStatusView, PedidoByIDView, PedidoDeleteView, 
                                             PedidoUpdateView)
from almoxarifado.views.produto_view import  (ProdutoListView, ProdutoCreateView, ProdutoDeleteView,
                                              ProdutoByNameView, ProdutoUpdateView)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #Usuarios
    path('usuarios/', UserListView.as_view(), name='usuarios'),
    path('register/', UserRegister.as_view(), name='register'),
	path('login/', UserLogin.as_view(), name='login'),
	path('logout/', UserLogout.as_view(), name='logout'),
	path('logged-user/', UserView.as_view(), name='logged-user'),
    #Modulos

    path('addmodulo-usuario/', AddModuleToUserView.as_view(), name='addmodulo-usuario'),
    path('modulos/', ModuleListView.as_view(), name='modulos'),
    path('modulos-create/', ModuleCreateView.as_view(), name='modulos-create'),
    path('modulos-delete/', ModuleDeleteView.as_view(), name='modulos-delete'),
    path('modulos-update/<int:pk>/', ModuleUpdateView.as_view(), name='modulos-update'),
    #Pedidos
    path('pedidos/', PedidoListView.as_view(), name='pedido-list'),
    path('pedidos-create/', PedidoCreateView.as_view(), name='pedido-create'),
    path('pedidos-usuario/', UserPedidoListView.as_view(), name='pedido-usuario'),
    path('pedidos-status/', PedidoByStatusView.as_view(), name='pedido-status'),
    path('pedidos-id/', PedidoByIDView.as_view(), name='pedido-id'),
    path('pedidos-delete/', PedidoDeleteView.as_view(), name='pedido-delete'),
    path('pedidos-update/<int:pk>/', PedidoUpdateView.as_view(), name='pedido-update'),
    #Produtos
    path('produto/s', ProdutoListView.as_view(), name='produto-list'),
    path('produtos-create/', ProdutoCreateView.as_view(), name='produto-create'),
    path('produtos-delete/', ProdutoDeleteView.as_view(), name='produto-elete'),
    path('produtos-nome/', ProdutoByNameView.as_view(), name='produto-nome'),
    path('produtos-update/<int:pk>', ProdutoUpdateView.as_view(), name='produto-update'),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
