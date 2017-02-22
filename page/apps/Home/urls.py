from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'home'),
    url(r'^datos$', views.Datos, name = 'datos'),
    url(r'^datos_update', views.Update_datos, name = 'get_more_datos'),
]