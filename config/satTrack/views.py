from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from sgp4.api import Satrec 
from sgp4.api import jday 
import pandas as pd 
from .extract_data import convert, get_live_data, data_over_time

def index(request):
    return render(request, 'home.html',)

def data(request):
    df, save_dict = convert('templates/tle.txt')
    TLE = """1 44804U 19081A   23208.14785096  .00005207  00000+0  24952-3 0  9992
2 44804  97.3437 265.0153 0010957 234.4970 125.5244 15.19295907203082"""

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


def data_buffer(request):
    TLE = """1 44804U 19081A   23208.14785096  .00005207  00000+0  24952-3 0  9992
2 44804  97.3437 265.0153 0010957 234.4970 125.5244 15.19295907203082"""
    print('____')
        # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        
        time_scale_pos = data_over_time(TLE, 120)
    
        if request.method == 'GET':
            return JsonResponse({'context': time_scale_pos})

        return JsonResponse({'status': 'Invalid request'}, status=400)
    else: 
        return 