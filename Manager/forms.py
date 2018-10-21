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
    weight1 = forms.IntegerField()
    weight2 = forms.IntegerField()
    weight3 = forms.IntegerField()
    weight4 = forms.IntegerField()
    weight5 = forms.IntegerField()
    weight6 = forms.IntegerField()
    weight7 = forms.IntegerField()
    weight8 = forms.IntegerField()
    weight9 = forms.IntegerField()
    weight10 = forms.IntegerField()
    capacityOfTruck = forms.IntegerField()
    class Meta:
        model = Home
        fields = ('source', 'destination1', 'destination2', 'destination3', 'destination4', 'destination5', 'destination6',
        'destination7', 'destination8', 'destination9', 'destination10', 'no_of_destinations', 'weight1', 'weight2', 'weight3',
        'weight4', 'weight5', 'weight6', 'weight7', 'weight8', 'weight9', 'weight10', 'capacityOfTruck')