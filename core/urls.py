from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('hospital', views.hospital, name='hos'),
    path('signup',views.signup,name='signup'),
    path('login',views.go,name='go'),
    path('prediction',views.prediction,name='prediction'),
    path('out',views.out,name='out')

]