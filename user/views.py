from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email    = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        newUser = User(username=username, email=email)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.add_message(request, messages.SUCCESS, 'Başarı ile kayıt olundu. Giriş Yapıldı')
        return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def LoginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Giriş Yapıldı.')
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'user/login.html',context)



    return render(request, 'user/dashboard.html')

def LogoutUser(request):
    if request.method =='POST':
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Oturumdan çıkış yapıldı.')
        return redirect('index')
