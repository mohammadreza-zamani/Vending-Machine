from django.urls import path
from . import views

urlpatterns = [
    path('', views.machines, name='machines'),
    path('reset', views.reset, name='reset'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('select/<int:id>', views.select, name='select'),
]
