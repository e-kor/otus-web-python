from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    login_form = AuthenticationForm(data=request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('courses:index'))

    context = {
        'title': 'вход',
        'login_form': login_form,
    }

    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('courses:index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        register_form = UserCreationForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'users/register.html', content)
