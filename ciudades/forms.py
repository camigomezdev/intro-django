from django import forms
from django.forms import TextInput, Textarea

from .models import Comment, City

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Author',
                'id': 'formName'
                }),
            'text': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Comment',
                'style': 'max-width: 300px;',
                'id': 'formComment'
                })
        }


class LikesForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('likes',)