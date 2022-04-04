from django.urls import path     
from . import views
# from . import views_forms

# http://127.0.0.1:8000/core/
app_name = 'core'

urlpatterns = [
    path('', views.indexcore, name='index'),	   
]