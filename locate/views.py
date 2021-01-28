from django.shortcuts import render
from .form import infoForm

# Create your views here.


def get_city(request):
    form = infoForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, 'getinfo.html', {'form':form})