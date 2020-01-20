from django.conf.urls import url
from . import views
from django.urls import include

urlpatterns = [
    url('Skill/', include('server.skill.urls')),
    url('Education/', include('server.education.urls')),
    url('Project/', include('server.project.urls')),
    url('Work/', include('server.work.urls')),
    url('Interest/', include('server.interest.urls')),
    url('Association/', include('server.association.urls')),
    url('', views.index, name='index'),
]