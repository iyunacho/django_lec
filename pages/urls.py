from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('mysite/activities/', views.activities),
    path('mysite/activities/summer/', views.summer),
    path('mysite/activities/winter/', views.winter),
    path('mysite/culture/', views.culture),
    path('mysite/cities/', views.cities),
    path('mysite/cities/vienna/', views.vienna),
    path('mysite/cities/graz/', views.graz),
    path('mysite/cities/salzburg/', views.salzburg),
]