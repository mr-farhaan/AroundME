from django.urls import path
from .views import*

urlpatterns =[
        path('reg/',Registration.as_view(),name="reg"),
        path('log/',Login.as_view(),name="log"),
]