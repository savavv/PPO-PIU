

from django.urls import path
from . import views  

urlpatterns = [
    path('api/data/', views.api_data, name='api_data'),  
]
