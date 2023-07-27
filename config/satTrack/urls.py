from django.urls import path 
from .views import index, data, data_buffer

urlpatterns = [
    path('', index, name='index'),
    path('data', data, name='data'),
    path('databuffer', data_buffer, name='databuffer')
    

]


"""

{longitude: 0.9616548576449437, latitude: -0.00008656854324213201, height: 35795.18276579048}
(index):96 Qe {x: 24130036.51326464, y: 34588006.94779447, z: -3647.1865759413568}
(index):97 Ct {dayNumber: 2460153, secondsOfDay: 22075.524000000005}

{latitude: -0.009016483744920674, longitude: 55.07495144405138, height: 35793.12098467509, iso_string: '2023-07-26T20:07:21Z'}
Qe {x: 24151473.434803497, y: -3800.652880351334, z: 34553004.48099303}
(index):87 Ct {dayNumber: 2460152, secondsOfDay: 29278}
"""