from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import CustomUser
from django.urls import reverse

# Create your views here.
PATH_TO_CALC = '../../calc'
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect(PATH_TO_CALC)
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
