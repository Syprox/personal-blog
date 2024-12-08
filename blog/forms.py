# blog/forms.py

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ваше ім'я"}
        ),
    )
    message = forms.CharField(
        widget=SummernoteWidget()
    )