from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,AbstractUser
import json,sys
import models


def index(request):
    return render_to_response('index.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            request.session['error'] = ['invalid passowrd or username']
            return HttpResponseRedirect('/login_gui')
    return HttpResponseRedirect('/')

@csrf_exempt
def login_gui(request):
    return render_to_response('login.html')

@login_required
@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def registerDoctor(dict_info):
    if dict_info.get('name') and dict_info.get('pwd'):
        doctor = models.Doctor()


def registerPaitent(dict_info):
    if dict_info.get('name') and dict_info.get('pwd'):
        patient = models.Patient()

def register(request):
    person_clas = request.POST['clas']
    if person_clas == 'd':
        return registerDoctor(request.POST)
    elif person_clas == 'p':
        return registerPaitent(request.POST)
    else :
        return render('type error')

def register_gui(request):
    return render_to_response('register.html')

def display_gui(request):
    return render_to_response('display.html')

def updateinfo_gui(request):
    return render_to_response('updateinfo.html')

def UserInfo(request):
    if request.POST:
        persion_clas = request.POST.get('clas')
        if persion_clas == 'd':
            return
        elif persion_clas == 'p':
            return
    elif request.GET:
        persion_clas = request.GET.get('clas')

from rest_framework import viewsets
from serializers import DoctorSer , PatientSer
class DoctorViewSet(viewsets.ModelViewSet):
    query_set = models.Doctor.objects.all().order_by('username')
    serializer_class = DoctorSer

class PatientViewSet(viewsets.ModelViewSet):
    query_set = models.Patient.objects.all()
    serializer_class = PatientSer
