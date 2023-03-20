from django import forms
from .models import Bio,Posts,Comments

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
        }

class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=100,label="Current Password",widget=forms.PasswordInput)
    new_password=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image","caption"]
        widgets={
            # "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"})
        }