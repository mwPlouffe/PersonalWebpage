from django.conf.urls import url
from . import views

urlpatterns = [
    url('OperatingSystems/', views.operatingSystems, name='operatingSystems'),
    url('Applications/', views.applications, name='applications'),
    url('ProgrammingLanguages/', views.programmingLanguages, name='programmingLanguages'),
    url('Platforms/', views.platforms, name='platforms'),
    url('Methodologies/', views.methodologies, name='methodologies'),
    url('Languages/', views.languages, name='languages'),
    url('Licenses/', views.licenses, name='licenses'),
    url('', views.index, name='index'),
]
