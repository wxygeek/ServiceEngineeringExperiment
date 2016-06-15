import views
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$',views.login),
    url(r'^login_gui', views.login_gui),
    url(r'^register', views.register),
    url(r'^register_gui', views.register_gui),
    url(r'^display_gui', views.display_gui),
    url(r'^updateinfo_gui', views.updateinfo_gui),
    url(r'^schema', views.schema),
    url(r'^get_schema_list', views.schema_list),
]
