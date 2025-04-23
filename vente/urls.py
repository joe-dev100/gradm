from django.urls import path
from .views import *

app_name = 'vente'
urlpatterns = [
    path('session/list/', session_list, name='session_list'),  
    path('session/update/<int:pk>/', session_update, name='session_update'),  
]
