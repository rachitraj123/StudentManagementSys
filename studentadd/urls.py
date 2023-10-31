from django.urls import path
from .views import *


app_name = 'studentadd'

urlpatterns = [
    path('',index,name = 'index'),
    path('accounts/login/',Login,name = 'login'),
    path('accounts/register/',Registerform,name = 'register'),
    path('accounts/logout/',Logout,name = 'logout'),
]