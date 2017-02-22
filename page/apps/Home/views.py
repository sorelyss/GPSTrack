from django.shortcuts import render
from . import models
# Create your views here.
def main(request):
	return render(request, 'home.html')

def Datos(request):
	syrus_data = models.Data.objects.last()
	return render(request, 'datos.html',{'s':syrus_data})

def Update_datos(request):
	#hacer el if id cambia (aumenta)...
	current_id = int(request.GET['current_id'])
	new_syrus_data = models.Data.objects.last()
	print new_syrus_data.id
	if new_syrus_data.id > current_id:
		return render(request, 'get_more_datos.html', {'s': new_syrus_data, 'Tflag': True})
	else:
		return render(request, 'get_more_datos.html', {'s': new_syrus_data, 'Fflag': False})