from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/', views.DefaultView, 'index')

urlpatterns = [
    path('api/skill/', include('server.skill.urls')),
    path('api/education/', include('server.education.urls')),
    path('api/project/', include('server.project.urls')),
    path('api/work/', include('server.work.urls')),
    path('api/interest/', include('server.interest.urls')),
    path('api/association/', include('server.association.urls')),
    path('api/', include(router.urls))
]