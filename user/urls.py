from django.urls import path
from user.views import*

urlpatterns =[
    path('',UserHome.as_view(),name="uh"),
    path('profile/',ProfileView.as_view(),name="pro"),
    path('addbio/',BioView.as_view(),name="bio"),
    path('cp/',ChangePassword.as_view(),name='cp'),
    path('mp/',MyPost.as_view(),name='mp'),
    path('editbio/<int:pk>/',EditBio.as_view(),name='editbio'),
    path('editpost/<int:pk>/',EditPost.as_view(),name='ep'),
    path('dp/<int:pk>/',DeletePost.as_view(),name='dp'),
    path("addcmnt/<int:pid>",addcomment,name="addc"),
    path("addlike/<int:pid>",addlike,name="addl"),
]