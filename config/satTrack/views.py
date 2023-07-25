from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from sgp4.api import Satrec 
from sgp4.api import jday 
import pandas as pd 
from .extract_data import convert, get_live_data

def index(request):
    return render(request, 'home.html',)

def data(request):
    df, save_dict = convert('templates/tle.txt')
    TLE = """1 44804U 19081A   23196.35840878  .00005378  00000+0  25694-3 0  9994
2 44804  97.3450 253.5493 0009838 278.3489  81.6631 15.19397374201298"""

        # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        position = get_live_data(TLE)
        if request.method == 'GET':
            return JsonResponse({'context': position})
        return JsonResponse({'status': 'Invalid request'}, status=400)
        
    else:
        context = {'data': save_dict}
        return render(request, 'data.html', context)
