from django.utils import timezone
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        time = timezone.now()
        fields = ['title', 'content']