from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import RegForm,Logform
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

# class MainHome(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"main_home.html")

class MainHome(TemplateView):
    template_name="main_home.html"


# class Registration(View):
#     form_class=RegForm
#     template_home="registration.html"
#     model=User
#     success_url="h"
#     def get(self,request,*args,**kwargs):
#         f=self.form_class()
#         return render(request,"registration.html",{"form":f})

#     def post(self,request,*args,**kwargs):
#         f=self.form_class()
#         if f.is_valid():
#             f.save()
#             messages.success(request,"User Registrated Successfully!!")
#             return redirect("h")
#         else:
#             messages.error(request,"Registration Failed")
#             return render(request,"registration.html",{"form":f})


class Registration(CreateView):
    form_class=RegForm
    template_name="registration.html"
    model=User
    success_url=reverse_lazy("h")
    



# class Login(View):
#     def get(self,request,*args,**kwargs):
#         f=Logform()
#         return render(request,'login.html',{'form':f})
#     def post(self,request,*args,**kwargs):
#         form_data=Logform(data=request.POST)
#         if form_data.is_valid():
#             us=form_data.cleaned_data.get("username")
#             ps=form_data.cleaned_data.get("password")
#             user=authenticate(request,username=us,password=ps)
#             if user:
#                 login(request,user)
#                 messages.success(request,"LOGIN SUCCESSFULLY!!")
#                 return redirect("uhome")
#             else:
#                 messages.error(request,"username or password incorrect")
#                 return render(request,"login.html",{"form":form_data})
#         else:
#             messages.error(request,"LOGIN FAILED!!")
#             return render(request,"login.html",{"form":form_data})


class Login(FormView):
    template_name="login.html"
    form_class=Logform
    def post(self,request,*args,**kwargs):
        form_data=Logform(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=ps)
            if user:
                login(request,user)
                messages.success(request,"LOGIN SUCCESSFULLY!!")
                return redirect("uhome")
            else:
                messages.error(request,"username or password incorrect")
                return render(request,"login.html",{"form":form_data})
        else:
            messages.error(request,"LOGIN FAILED!!")
            return render(request,"login.html",{"form":form_data})

            
