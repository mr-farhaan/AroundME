from django.urls import path
from .views import*

urlpatterns=[
    path('uhome/',Userhome.as_view(),name='uhome'),
    path('profile/',Profileview.as_view(),name='profile'),
    path('bio/',BioView.as_view(),name='bio'),
]