from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ciudades.models import City

from .forms import CommentForm, LikesForm


def ciudad(request, id=None):
    city = City.objects.get(id=id)
    new_comment(request, id)
    form = CommentForm()
    return render(request, 'city.html', {'city': city, 'form': form})


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
        return redirect('ciudad', id=id)

    return redirect('ciudad', id=id)


@login_required
def add_like(request, id=None):
    if request.method == "POST":
        city = City.objects.get(id=id)
        like = True
        for like in city.likes.all():
            print("##### this view is called")
            if like == request.user:
                like = False
                city.likes.remove(request.user)

        if like:
            city.likes.add(request.user)

        return redirect('ciudad', id=id)
    else:
        return redirect('ciudad', id=id)
