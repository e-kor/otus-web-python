from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Student


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


def register_(request):
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


@swagger_auto_schema(methods=['post'], request_body=TokenObtainPairSerializer)
@api_view(['POST'])
def register(request: Request):
    credentials = request.data
    try:
        student = Student.objects.create(username=credentials['username'])
        password = credentials['password']
        validate_password(password)
        student.set_password(password)
        return Response({'detail': "OK"})
    except IntegrityError:
        raise MethodNotAllowed(method="register", detail="user with such username is already registered")
    except ValidationError as e:
        student.delete()
        raise MethodNotAllowed(method="registe", detail=f"password not passed validation: {e}")
