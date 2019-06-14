from django import forms
from . import globalvalues
from .models import Calculator

class hey_CalculatorForm(forms.Form):
    """docstring for Calculator"""
    GENDER         = globalvalues.get_gender()
    RACE           = globalvalues.get_race()
    FAMILY_HX      = globalvalues.get_family_hx()
    SMOKER         = globalvalues.get_smoking_status()
    IS_STEROID     = globalvalues.get_steroid_status()
    IS_DM          = globalvalues.get_dm_status()
    IS_TREATED_HTN = globalvalues.get_treated_htn_status()

    ###### General Information (won't change over time)######
    gender = forms.ChoiceField(choices=GENDER)
    race   = forms.ChoiceField(choices=RACE)

    ###### Parameters for undiagnosed DM ######
    weight     = forms.IntegerField()
    height     = forms.IntegerField()
    family_hx  = forms.ChoiceField(choices=FAMILY_HX)
    is_steroid = forms.ChoiceField(choices=IS_STEROID)


    ###### Parameters for 10-year CV and stroke risk ######
    tc    = forms.IntegerField()
    hdl   = forms.IntegerField()
    sbp   = forms.IntegerField()
    dbp   = forms.IntegerField()
    is_dm = forms.ChoiceField(choices=IS_DM)

    ###### Parameters for both calculator ######
    # TODO only 40-79 y/o for 10-year cv and strke risk
    age            = forms.IntegerField()
    is_treated_htn = forms.ChoiceField(choices=IS_TREATED_HTN)
    smoker         = forms.ChoiceField(choices=SMOKER)

class CalculatorForm(forms.ModelForm):
    class Meta:
        model  = Calculator
        fields = '__all__'



