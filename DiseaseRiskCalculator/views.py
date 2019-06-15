from django.shortcuts import render, redirect
from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import CustomUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return redirect('../admin')
        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
