from django.urls import path
from account.views import*

urlpatterns =[
    path('',MainHome.as_view()),
    path('Reg/',Reg.as_view(),name='reg'),
    path('log/',Log.as_view(),name='log'),
    path('lgout/',LogOut.as_view(),name='lgout'),

]