from django.shortcuts import render, HttpResponse
from sgp4.api import Satrec 
from sgp4.api import jday 
import pandas as pd 
from .extract_data import convert

def index(request):
    return render(request, 'home.html',)

def data(request):
    df, save_dict = convert('templates/tle.txt')
  
    # save_dict = save_dict.to_html()
    context = {'data': save_dict}
    
  
    return render(request, 'data.html', context)
