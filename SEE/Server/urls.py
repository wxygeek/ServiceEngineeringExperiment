import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$',views.login),
    url(r'^login_gui', views.login_gui),
    url(r'^register', views.register),
    url(r'^register_gui', views.register_gui),
    url(r'^display_gui', views.display_gui),
    url(r'^updateinfo_gui', views.updateinfo_gui),
]
