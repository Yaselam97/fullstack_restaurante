from django.urls import path
from . import views

urlpatterns = [
    path('', views.dishes),
    path('contattaci/', views.contattaci, name='contattaci'),
]