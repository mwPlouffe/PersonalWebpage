from django.conf.urls import url
from . import views

urlpatterns = [
    url('Short/', views.shortEducation, name='shortEducation'),
    url('Long/', views.longEducation, name='longEducation'),
]