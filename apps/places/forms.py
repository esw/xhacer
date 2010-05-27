from django.utils.translation import ugettext_lazy as _
from django import forms
from models import *
#from uni_form.helpers import FormHelper, Submit, Reset

class PlaceForm(forms.ModelForm):
    # uni_form FormHelper
    #helper = FormHelper()

    #submit = Submit('Guardar','Guardar Sitio')
    #helper.add_input(submit)
    #cancel = Reset('Cancelar','Cancelar')
    #helper.add_input(cancel)

    class Meta:
        model = Place
        exclude = ('slug','active')

class PlaceCityForm(PlaceForm):
    lat = forms.FloatField(widget=forms.HiddenInput)
    lon = forms.FloatField(widget=forms.HiddenInput)
    class Meta:
        model = Place
        exclude = ('slug','active','city')
