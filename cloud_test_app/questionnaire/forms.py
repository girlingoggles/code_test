from django import forms
from django.forms import ModelForm
from .models import FilledQuestionnaire

class Dropdown(ModelForm): 
    class Meta:
        model = FilledQuestionnaire 
        fields = ['month',  'day']
        #day = forms.ChoiceField(choices=
        #month = forms.ModelChoiceField(queryset=Part.objects.order_by('month').values_list('month', flat=True).distinct())
 
        #day = forms.ModelChoiceField(queryset=Part.objects.order_by('day').values_list('day', flat=True).distinct())