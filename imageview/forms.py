from django import forms
from .models import Imageview

class PostForm(forms.ModelForm):
    class Meta:
        model = Imageview
        fields = ('title', 'description', 'image')
