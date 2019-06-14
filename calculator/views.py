from django.shortcuts import render
from .forms import CalculatorForm
from . import riskcalc

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        print(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi = round(weight / (height**2)  * 10000, 2)
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            race = form.cleaned_data['race']
            family_hx = form.cleaned_data['family_hx']
            is_steroid = form.cleaned_data['is_steroid']
            tc = form.cleaned_data['tc']
            hdl = form.cleaned_data['hdl']
            sbp = form.cleaned_data['sbp']
            dbp = form.cleaned_data['dbp']
            is_dm = form.cleaned_data['is_dm']
            is_treated_htn = form.cleaned_data['is_treated_htn']
            smoker = form.cleaned_data['smoker']
            ascvd_risk = riskcalc.get_ascvd_risk(age, is_dm, gender, race,
                                                 smoker, tc, hdl, sbp,
                                                 is_treated_htn)
            dm_risk = riskcalc.get_dm_risk(age, gender, is_treated_htn,
                                           is_steroid, smoker, family_hx, bmi)

            return render(request, 'calculator.html',
                          {'form': form, 'bmi': bmi,
                           'ascvd_risk': ascvd_risk, 'dm_risk': dm_risk})

    else:
        form = CalculatorForm()
    return render(request, 'calculator.html', {'form': form})


