from django.conf.urls import url
from . import views

urlpatterns = [
    url('ExperienceAbroad/', views.ExperienceAbroad, name='ExperienceAbroad'),
    url('Literature/', views.Literature, name='Literature'),
    url('Sports/', views.Sports, name='Sports'),
    url('Passions/', views.Passions, name='Passions'),
]