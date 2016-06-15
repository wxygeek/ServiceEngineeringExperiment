from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
import json,sys

def index(requests):
    return render_to_response('index.html')
