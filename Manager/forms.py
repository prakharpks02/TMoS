from django import forms
from Manager.models import Home

class HomeForm(forms.ModelForm):
    source = forms.CharField()
    destination = forms.CharField()
    class Meta:
        model = Home
        fields = ('source', 'destination',)