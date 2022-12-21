from django.urls import  path
from . import  views
from .views import homepage

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('new/',views.new,name='new'),
    path('form/', views.form, name='form'),

]


