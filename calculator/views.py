from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import CalculatorForm
from .models import CalculatorModel
from . import globalvalues
from user.models import CustomUser
from . import riskcalc
from datetime import date
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def calculator(request):
    data = {'date': [], 'bmi': [], 'sbp': [], 'dbp': []}
    objects = None
    risk_dict = {'bmi': ' ', 'ascvd_risk': ' ', 'dm_risk': ' '}
    gender, race, age, tc, hdl= None, None, None, None, None
    height, weight = None, None
    is_dm = False
    is_treated_htn = False
    is_steroid = False
    smoker = 0
    family_hx = 0

    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            risk_dict = _calculate_risk(form)
            # update or save data
            if request.user.is_active:
                all_dict = {'uid': request.user, 'date': date.today()}
                all_dict.update(risk_dict)
                all_dict.update(form.cleaned_data)
                obj, is_created = CalculatorModel.objects.update_or_create(
                    date = date.today(), uid_id = request.user.id, defaults=all_dict)
    else: # method == 'GET'
        # is_active is set to False if the account is deleted
        # so we need to check if the user is still active
        form = CalculatorForm()

    if request.user.is_active:
        gender = request.user.gender
        race = request.user.race
        age = date.today().year - request.user.birthyear

        # use objects for Chart.js function
        objects = _filter_data_by_uid(request.user.id)
        for o in objects:
            str_date = o.date.strftime("%m/%d/%Y")
            data['date'].append(str_date)
            data['bmi'].append(o.bmi)
            data['sbp'].append(o.sbp)
            data['dbp'].append(o.dbp)
            is_dm = o.is_dm
            is_treated_htn = o.is_treated_htn
            is_steroid = o.is_steroid
            hdl = o.hdl
            tc = o.tc
            smoker = o.smoker
            family_hx = o.family_hx
            height = o.height
            weight = o.weight


    return render(request, 'calculator.html',
                  {'form': form, 'bmi': risk_dict['bmi'],
                   'ascvd_risk': risk_dict['ascvd_risk'],
                   'dm_risk': risk_dict['dm_risk'],
                   'gender': gender, 'race': race, 'age': age, 'is_dm': is_dm,
                   'is_treated_htn': is_treated_htn, 'is_steroid': is_steroid,
                   'hdl': hdl, 'tc': tc, 'smoker': smoker, 'height': height,
                   'weight': weight,
                   'family_hx': family_hx, 'data': json.dumps(data)})


def _filter_data_by_uid(uid):
    try:
       objects = CalculatorModel.objects.filter(uid_id=uid)
       return objects
    except ObjectDoesNotExist:
        print('uid not found')


def _calculate_risk(form):
    """
    Input: already valid form
    return: risks in dict
    """
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
    is_dm = form.cleaned_data['is_dm']
    is_treated_htn = form.cleaned_data['is_treated_htn']
    smoker = form.cleaned_data['smoker']
    ascvd_risk = riskcalc.get_ascvd_risk(age, is_dm, gender, race,
                                         smoker, tc, hdl, sbp,
                                         is_treated_htn)
    dm_risk = riskcalc.get_dm_risk(age, gender, is_treated_htn,
                                   is_steroid, smoker, family_hx, bmi)
    return {'ascvd_risk': ascvd_risk, 'dm_risk': dm_risk, 'bmi': bmi}
