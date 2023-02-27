from django.urls import path
from .views import*

urlpatterns=[
    path('uhome/',Userhome.as_view(),name='uhome')
]