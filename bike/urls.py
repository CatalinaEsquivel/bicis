from django.urls import path
from .views import index, iniciosesion, registro, bicicletas
urlpatterns = [
    path('', index, name='admin-index'),
    path('bicicletas/', bicicletas, name='bicicletas'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('registro/', registro, name='registro'),
]