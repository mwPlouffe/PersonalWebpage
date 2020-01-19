from django.conf.urls import url
from . import views

urlpatterns = [
    url('Short/', views.shortWork, name='shortWork'),
    url('Volunteer/Short/', views.shortVolunteerWork, name='shortVolunteerWork'),
    url('Long/', views.longWork, name='LongWork'),
    url('Volunteer/Long/', views.longVolunteerWork, name='LongVolunteerWork'),
]