from django.shortcuts import render, HttpResponse
from .form import getLocationDataForm
from .persistence import getdatabyCity

# Create your views here.


def get_city(request):
    form = getLocationDataForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        byCity = getdatabyCity(form)
        return HttpResponse(byCity)

    return render(request, 'getinfo.html', {'form':form})