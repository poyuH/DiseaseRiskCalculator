from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import CalculatorForm
from .models import CalculatorModel
from . import globalvalues
from user.models import CustomUser
from . import riskcalc
from datetime import date

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        objects = None
        form = CalculatorForm(request.POST)
        if form.is_valid():
            risk_dict = _calculate_risk(form)
            # update or save data
            if request.user.is_authenticated:
                all_dict = {'uid': request.user, 'date': date.today()}
                all_dict.update(risk_dict)
                all_dict.update(form.cleaned_data)
                obj, is_created = CalculatorModel.objects.update_or_create(
                    date = date.today(), uid_id = request.user.id, defaults=all_dict)
                # use objects for graph function
                objects = _filter_data_by_uid(request.user.id)

            return render(request, 'calculator.html',
                          {'form': form, 'bmi': risk_dict['bmi'],
                           'ascvd_risk': risk_dict['ascvd_risk'],
                           'dm_risk': risk_dict['dm_risk'],
                           'objects': objects})

    else: # method == 'GET'
        gender, race, age = None, None, None
        objects = None
        if request.user.is_active:
            gender = request.user.gender
            race = request.user.race
            age = date.today().year - request.user.birthyear
            # use objects for graph function
            objects = _filter_data_by_uid(request.user.id)

        # is_active set to False if the account is deleted
        # No need for checking authenticated
        """
        elif request.user.is_authenticated:
            try:
                obj = CustomUser.objects.get(email=request.user.email)
            except :
                print('can\'t find user by email')
            gender = obj.gender
            race = obj.race
            age = date.today().year - obj.birthyear
        """

        form = CalculatorForm(initial=
                              {'gender': gender, 'race': race, 'age': age})
        return render(request, 'calculator.html',
                      {'form': form, 'objects': objects})


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
