from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from .forms import BioForm,ChangePasswordForm,PostForm,CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Bio,Posts,Comments


# Create your views here.

# class UserHome(View):
#     def get(self,request):
#         return render(request,"userhome.html")
class UserHome(CreateView):
    template_name="userhome.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("uh")
    def form_valid(self,form):
         form.instance.user=self.request.user
         messages.success(self.request,"Post Uploaded!!")
         self.object=form.save()
         return super().form_valid(form)
    def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         context["data"]=Posts.objects.all().order_by('-datetime')
         context["cform"]=CommentForm()
         context["comments"]=Comments.objects.all()
         return context
def addcomment(request,*args,**kwargs):
         if request.method=="POST":
              pid=kwargs.get("pid")
              post=Posts.objects.get(id=pid)
              user=request.user
              cmnt=request.POST.get("comment")
              Comments.objects.create(comment=cmnt,user=user,post=post)
              return redirect("uh")
         
def addlike(request,*args,**kwargs):
     pid=kwargs.get("pid")
     post=Posts.objects.get(id=pid)
     user=request.user
     post.likes.add(user)
     post.save()
     return redirect("uh")         
    
class ProfileView(TemplateView):
    template_name="profile.html"

class BioView(CreateView):
    form_class=BioForm
    template_name="addbio.html"
    model=Bio
    success_url=reverse_lazy("pro")    
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"Bio Added!!")
        return super().form_valid(form)
    
class EditBio(UpdateView):
    form_class=BioForm
    model=Bio
    template_name="editbio.html"
    success_url=reverse_lazy('pro')
    pk_url_kwargs="pk"
    # def form_valid(self,form):
    #     form.instance.user=self.request.user
    #     self.object=form.save()
    #     return super().form_valid(form)    

class ChangePassword(FormView):
        template_name="change_password.html"
        form_class=ChangePasswordForm
        def post(self,request,*args,**kwrgs):
             form_data=ChangePasswordForm(data=request.POST)
             if form_data.is_valid():
                  current=form_data.cleaned_data.get("current_password")
                  new=form_data.cleaned_data.get("new_password")
                  confirm=form_data.cleaned_data.get("confirm_password")
                  print(current)
                  user=authenticate(request,username=request.user.username,password=current)
                  if user:
                    if new==confirm:
                            user.set_password(new)
                            user.save()
                            messages.success(request,"Password Changed!!!")
                            logout(request)
                            return redirect("log")
                    else:
                            messages.error(request,"Password Mismatches!!")
                            return redirect("cp")
                  else:
                       messages.error(request,"Incorrect Password!!!")
                       return redirect("cp")
             else:
                  return render(request,"change_password.html",{"form":form_data})    

class MyPost(TemplateView):
     template_name="mypost.html"
     def get_context_data(self, **kwargs):
         context=super().get_context_data(**kwargs)
         context["data"]=Posts.objects.filter(user=self.request.user).order_by('-datetime')
         return context  
     
class EditPost(UpdateView):
    form_class=PostForm
    model=Posts
    template_name="editpost.html"
    success_url=reverse_lazy('mp')
    pk_url_kwargs="pk"     

class DeletePost(DeleteView):
    model=Posts
    template_name="deletepost.html"
    success_url=reverse_lazy('mp')