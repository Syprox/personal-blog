# blog/forms.py

from django import forms
from .models import Image


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ваше ім'я"}
        ),
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Додайте коментар!"}
        )
    )

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

""" from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget()) """