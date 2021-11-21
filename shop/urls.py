from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),   #chama a lista de produto sem parâmetros
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),   #chama a lista de produtos com o parâmetro de categoria, para filtrar os produtos pela categoriaS
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),   #passa o id e o slug para acessar um produto específico
]
