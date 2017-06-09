from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
import json
from datetime import datetime, timedelta

def main(request):
	return render(request, 'home.html')

def Historial(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end))).order_by('date')
	return render(request, 'historial.html',{'syrus_data':syrus_data})

def Fechas(request):
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date)).order_by('date')
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	alturas = [s.elevation for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas, 'alturas': alturas})


def Historial_Cel(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.raw("SELECT * FROM android_data WHERE (date BETWEEN '%s' AND '%s') ORDER BY date;"%(start,end))
	for s in syrus_data:
		print(s.gps_id)
	return render(request, 'historial_cel.html',{'syrus_data':syrus_data})

def Fechas_Cel(request):
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.raw("SELECT * FROM android_data WHERE (date BETWEEN '%s' AND '%s') ORDER BY date;"%(start_date,end_date))
	enviar = [{'lat': str(s.longitude), 'lng': str(s.latitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas})


def TiempoReal(request):
	syrus_data = models.Data.objects.last()
	return render(request, 'real_time.html',{'s':syrus_data})

def Update(request):
	current_id = int(request.GET['current_id'])
	s = models.Data.objects.last()
	print s.id
	if s.id > current_id:
		enviar = "({lat: %s, lng: %s})"%(s.latitude, s.longitude)
		#return HttpResponse(enviar)
		return JsonResponse({'puntos': enviar, 'id':s.id, 'date': s.date.strftime("%I:%M:%S"), 'elevation': s.elevation})
	else:
		return HttpResponse("no")

def Historial_by_area(request):
	syrus_data = models.Data.objects.all()
	return render(request, 'historial_by_area.html',{'syrus_data':syrus_data})

def Area(request):
	start_lat = request.GET['start_lat']; start_lng = request.GET['start_lng']
	end_lat = request.GET['end_lat']; end_lng = request.GET['end_lng']
	start_lat= "+"+start_lat
	end_lat= "+"+end_lat
	syrus_data = models.Data.objects.filter(latitude__range=(start_lat, end_lat),longitude__range=(start_lng, end_lng)).order_by('date')
	#SELECT * FROM Home_data WHERE (latitude BETWEEN 11.0196 AND 11.0198) AND (longitude BETWEEN -74.8508 AND -74.8506); 
	#COMO FUNCIONA: syrus_data = models.Data.objects.filter(latitude__range=("+10.998","+10.999"),longitude__range=("-74.80722","-74.80730"))
	print syrus_data
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	return JsonResponse({'puntos':str(enviar).replace("'",""), 'fechas': dic_fechas})

def Historial_Area(request):
	#end = datetime.now().strftime('%B %d, %Y - %H:%M:%S'); start = (datetime.now()-timedelta(weeks=4)).strftime('%B %d, %Y - %H:%M:%S')
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end)) ).order_by('date')
	#syrus_data = models.Data.objects.all().order_by('-id')[:30][::-1] #Los ultimos 30 datos
	#syrus_data = models.Data.objects.all() #Todos los datos en la base
	#print syrus_data[1].date
	return render(request, 'historial_area.html',{'syrus_data':syrus_data})

def Fechas_Area(request):
	start_date = request.GET['start_date']
	print start_date
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date)).order_by('date')
	enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date for s in syrus_data]
	return JsonResponse({'puntos': str(enviar).replace("'",""), 'date': dic_fechas})

def Elevacion(request):
	end = datetime.now()
	start = datetime.now() - timedelta(weeks=4)
	syrus_data = models.Data.objects.filter(date__range=(str(start),str(end))).order_by('date')
	return render(request, 'elevacion.html',{'syrus_data':syrus_data})

def Altura(request):
	start_date = request.GET['start_date']
	end_date = request.GET['end_date']
	syrus_data = models.Data.objects.filter(date__range=(start_date, end_date)).order_by('date')
	#enviar = [{'lat': str(s.latitude), 'lng': str(s.longitude)} for s in syrus_data]
	dic_fechas = [s.date.strftime("%B %d, %Y, %I:%M%p") for s in syrus_data]
	alturas = [s.elevation for s in syrus_data]
	longitudes = [s.latitude for s in syrus_data]
	latitudes = [s.longitude for s in syrus_data]
	return JsonResponse({'alturas': alturas,'longitudes': longitudes, 'latitudes': latitudes})
