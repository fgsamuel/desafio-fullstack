from django.urls import path, include
from rest_framework import routers

from desafio_fullstack.core.views import estados_list, estados_create, estados_update, estados_delete, cidades_list, \
    cidades_update, cidades_delete, cidades_create
from desafio_fullstack.core.views_api import EstadoViewSet, CidadeViewSet

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)

urlpatterns = [
    path('estados/', estados_list, name='estados_list'),
    path('estados/create/', estados_create, name='estados_create'),
    path('estados/update/<int:estado_pk>/', estados_update, name='estados_update'),
    path('estados/delete/<int:estado_pk>/', estados_delete, name='estados_delete'),
    path('cidades/', cidades_list, name='cidades_list'),
    path('cidades/create/', cidades_create, name='cidades_create'),
    path('cidades/update/<int:cidade_pk>/', cidades_update, name='cidades_update'),
    path('cidades/delete/<int:cidade_pk>/', cidades_delete, name='cidades_delete'),
    path('api/', include(router.urls)),
]
