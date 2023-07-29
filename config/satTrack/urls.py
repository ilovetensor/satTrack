from django.urls import path 
from .views import data, data_buffer, list_view, detail_view

urlpatterns = [

    path('sat', list_view.as_view(), name='list_view'),
    path('sat/<int:norad_id>', detail_view, name='detail_view'),
    path('data/<int:norad_id>', data, name='data',),
    path('databuffer/<int:norad_id>', data_buffer, name='databuffer')
    
]

