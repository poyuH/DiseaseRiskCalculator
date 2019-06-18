from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, path
from datetime import date

# Create your views here.
PATH_TO_CALC = '../../calc'
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            # directly login after register
            user = authenticate(request, username=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
            return redirect(PATH_TO_CALC)
        else:
            return render(request, 'register.html', {'form':form})
    else:
        age, gender, race = None, None, None
        if request.user.is_active:
            age = date.today().year - request.user.birthyear
            gender = request.user.gender
            race = request.user.race
        form = CustomUserCreationForm(
            initial={'age':age, 'gender':gender , 'race':race})
        return render(request, 'register.html', {'form': form})


def logout_redirect(request):
    logout(request)
    return redirect(PATH_TO_CALC)
