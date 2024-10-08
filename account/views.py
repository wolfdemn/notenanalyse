from audioop import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, user_login_failed
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'account/base.html')


def login_user(request):
    L_Form = AuthenticationForm()

    if request.method == 'POST':
        L_Form = AuthenticationForm(data=request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('account:index'))

    return render(request, 'account/../templates/notenanalyse/login.html', {'L_Form': L_Form})

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    R_Form = UserCreationForm()

    if request.method == 'POST':
        # print(request.POST)

        R_Form = UserCreationForm(request.POST)
        if R_Form.is_valid():
            R_Form.save()

            name = R_Form.cleaned_data['username']
            password = R_Form.cleaned_data['password1']
            user = authenticate(request, username=name, password=password)
            if user:
                login(request, user)
                return redirect(reverse('notenanalyse:dashboard'))

    return render(request, 'account/../templates/notenanalyse/register.html', {'R_Form': R_Form})

def me(request):
    if request.user:
        if request.user.is_authenticated: # Check, if user is authenticated

            if request.method == 'POST':
                update_form = UserChangeForm(request.POST)
                if update_form.is_valid():
                    update_form.save()

            return render(request, './account/my-account.html', {'update_form': update_form})
        else: return redirect('login')
    return redirect('login')