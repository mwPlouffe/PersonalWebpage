from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'education', views.EducationView)

urlpatterns = [
    url('Short/', views.shortEducation, name='shortEducation'),
    url('Long/', views.longEducation, name='longEducation'),
]