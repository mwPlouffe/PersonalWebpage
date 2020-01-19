from django.conf.urls import url
from . import views

urlpatterns = [
    url('Short/', views.shortProject, name='shortProject'),
    url('Academic/Short/', views.shortAcademicProject, name='shortAcademicProject'),
    url('Long/', views.longProject, name='LongProject'),
    url('Academic/Long/', views.longAcademicProject, name='longAcademicProject'),
]