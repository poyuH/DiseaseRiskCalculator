from django import forms
from .models import CalculatorModel


class CalculatorForm(forms.ModelForm):
    class Meta:
        model  = CalculatorModel
        exclude = ['uid', 'date', 'ascvd_risk', 'bmi', 'dm_risk']

