from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('accounts/sign_login/',sign_login,name="sign_login"),
    path('dashboard/',dashboard,name="dashboard"),
    path('accounts/user_login/',user_login,name="user_login"),
    path('accounts/user_logout/',user_logout,name="user_logout"),
    path('detail/<slug:title>',detail,name="detail")
]
