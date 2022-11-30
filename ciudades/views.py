from django.shortcuts import render, redirect
from ciudades.models import City, Comment

from .forms import CommentForm


def ciudad(request, id=None):
    city = City.objects.get(id=id)
    new_comment(request, id)
    return render(request, 'city.html', {'city': city})

def ciudades(request):
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})

def new_comment(request, id=None):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment_value = form.save(commit=False)
            new_comment_value.city = City.objects.get(id=id)
            new_comment_value.save()

            return redirect('ciudad', id=id)
    else:
        form = CommentForm()

    return render(request, 'comments.html', {'form': form})