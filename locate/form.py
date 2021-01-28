from django.forms import ModelForm
from .models import Location


class getLocationDataForm(ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'zipcode']
