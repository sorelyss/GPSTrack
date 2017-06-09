from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name = 'home'),
    url(r'^historial$', views.Historial, name = 'historial'),
    url(r'^fecha', views.Fechas, name = 'fechas'),
    url(r'^real_time', views.TiempoReal, name = 'real_time'),
    url(r'^update', views.Update, name = 'update'),

    url(r'^historial_cel$', views.Historial_Cel, name = 'historial_cel'),
    url(r'^fec_cel', views.Fechas_Cel, name = 'fechas_cel'),

    url(r'^historial_area$', views.Historial_by_area, name = 'historial_by_area'),
    url(r'^areaquery', views.Area, name = 'area'),
    url(r'^historial_And_Area$', views.Historial_Area, name = 'historial_area'),
    url(r'^dat_area', views.Fechas_Area, name = 'fechas_area'),

    url(r'^elevacion$', views.Elevacion, name = 'elevacion'),
    url(r'^altura', views.Altura, name = 'altura')
    #url(r'^elevation$', views.Elevation, name = 'elevation'),    
]
