from django.urls import path
from plantilla33_app import views

urlpatterns = [
    path('', views.dashboard),
    path('wall/new', views.AddNewDev),
    path('wall/<int:id>/', views.ViewDev),
    path('wall/<int:id>/edit', views.EditDev),
    path('wall/<int:id>/update', views.UpdateDev),
    path('wall/<int:id>/destroy', views.DeleteDev)

]