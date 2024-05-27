# logapp/urls.py
from django.urls import path
from .views import index, get_log_data

urlpatterns = [
    path('', index, name='index'),
    path('get-log-data/', get_log_data, name='get-log-data'),
]
