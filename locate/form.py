from django.forms import ModelForm
from .models import location


class infoForm(ModelForm):
    class Meta:
        model = location
        fields = ['city']
