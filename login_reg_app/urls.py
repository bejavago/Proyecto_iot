from django.urls import path
# from . import views
from .views import LoginLocal, RegisterLocal
# from login_reg_app import views

app_name = 'login_reg_app'

urlpatterns = [
    
    path('', LoginLocal.as_view(), name='login'),
    path('register/', RegisterLocal.as_view(), name='register'),
    # path('', views.Login_Reg),
    # path('register', views.Register),
    # path('login', views.Login),
    # path('success', views.Success),
    # path('logout', views.Logout)
]