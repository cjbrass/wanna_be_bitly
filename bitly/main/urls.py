from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\w+)$', views.redirect, name='redirect'),
    url(r'^$', views.index, name='index'),
]