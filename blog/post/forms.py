from django import forms
from .models import Comments , Post

class CommentsForms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author','text'] 

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'image', 'category']