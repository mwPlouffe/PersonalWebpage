from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'index', views.DefaultView, 'index')

urlpatterns = [
    path('Skill/', include('server.skill.urls')),
    #url('Education/', include('server.education.urls')),
    #url('Project/', include('server.project.urls')),
    #url('Work/', include('server.work.urls')),
    path('Interest/', include('server.interest.urls')),
    path('Association/', include('server.association.urls')),
    path('', views.DefaultView.as_view({'get': 'index'}))
]