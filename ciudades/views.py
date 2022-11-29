from django.shortcuts import render
from ciudades.models import Ciudad


def ciudad(request, id=None):
    city = Ciudad.objects.get(id=id)
    print(city)
    return render(request, 'ciudad.html', {'city': city})

def ciudades(request):
    cities = Ciudad.objects.all()
    return render(request, 'ciudades.html', {'cities': cities})