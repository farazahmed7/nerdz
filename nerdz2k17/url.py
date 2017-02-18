from django.conf.urls import url
from nerdz2k17 import views

__author__ = 'abc'

urlpatterns = [
    url(r'^submit$', views.submit, name='showSem'),
    url(r'^signUp$', views.signup, name='signUp'),
    url(r'^signIn$', views.loginUser, name='loginUser'),



]
