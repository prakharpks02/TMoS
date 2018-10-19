from django import forms
from Manager.models import Home

class HomeForm(forms.ModelForm):
    source = forms.CharField()
    destination1 = forms.CharField()
    destination2 = forms.CharField()
    destination3 = forms.CharField()
    destination4 = forms.CharField()
    destination5 = forms.CharField()
    destination6 = forms.CharField()
    destination7 = forms.CharField()
    destination8 = forms.CharField()
    destination9 = forms.CharField()
    destination10 = forms.CharField()
    no_of_destinations = forms.IntegerField()
    class Meta:
        model = Home
        fields = ('source', 'destination1', 'destination2', 'destination3', 'destination4', 'destination5', 'destination6',
        'destination7', 'destination8', 'destination9', 'destination10', 'no_of_destinations')