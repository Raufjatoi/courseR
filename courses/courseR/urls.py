from django.contrib import admin
from django.urls import path
from .views import home, list, detail, register, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('courses/', list, name='list'),
    path('courses/<int:pk>/', detail, name='detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
