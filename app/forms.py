from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Enter City', max_length=100)
