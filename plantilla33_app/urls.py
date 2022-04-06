from django.urls import path
from plantilla33_app import views
from .views import AddNewDev, Dashboard, EditDev

from django.conf import settings 
from django.conf.urls.static import static 


app_name='plantilla33_app'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('wall/new', AddNewDev.as_view(), name='new_device'),
    path('wall/<int:id>/', views.ViewDev),
    path('wall/<int:id>/edit', EditDev.as_view(), name='edit_device'),
    path('wall/<int:id>/update', views.EditDev.as_view(), name='update_device'),
    path('wall/<int:id>/destroy', views.DeleteDev),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
