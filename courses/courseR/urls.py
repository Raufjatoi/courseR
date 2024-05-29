from django.contrib import admin
from django.urls import path
from .views import home, c_list, detail, register, login_view, logout_view

urlpatterns = [
    path('', home , name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('courses/<int:pk>/', detail, name='detail'),
    path('courses/', c_list,  name='list' )
]
