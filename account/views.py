from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import*
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

# class MainHome(View):
#     def get(self,request,*args,**kwrgs):
#         return render(request,"mainhome.html")

class MainHome(TemplateView):
    template_name="mainhome.html"

# class Reg(View):
#     def get(self,request,*args,**kwrgs):
#         f=RegForm()
#         return render(request,"registration.html",{'form':f}) 
#     def post(self,request,*args,**kwrgs):
#         f=RegForm(data=request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request,"User Registration Successfully!!")
#             return redirect("h")
#         else:
#             messages.error(request,"Registration failed")
#             return render(request,"registration.html",{'form':f})  

class Reg(CreateView):
    form_class=RegForm
    template_name="registration.html"
    model=User
    success_url=reverse_lazy("h")  
    def form_valid(self,form):
        mail=form.cleaned_data.get("email")
        send_mail(
            "Around Me Registration",
            "Welcome to Around Me!!",
            "farhananu121@gmail.com",
            [mail]
        )
        messages.success(self.request,"Registration Completed!!!")
        self.objects=form.save()
        return super().form_valid(form)

# class Log(View):
#     def get(self,request,*args,**kwrgs):
#         f=LogForm()
#         return render(request,"login.html",{"form":f})

class Log(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwrgs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")    
            ps=form_data.cleaned_data.get("password") 
            user=authenticate(request,username=us,password=ps)
            if user:
                login(request,user)
                messages.success(request,"Login Successfully!!")
                return redirect("uh")
            else:
                messages.error(request,"incorrect username or password")
                return render(request,"login.html",{"form":form_data})  
        else:
            messages.error(request,"Login failed")
            return render(request,"login.html",{"form":form_data})  
        
class LogOut(View):
    def get(self,request):
        LogOut=(request)
        return redirect("log.html")

            
