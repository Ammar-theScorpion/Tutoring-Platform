from django import forms
from django.forms import ModelForm

from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image_url", "tags"]
        labels = {"body": "Caption", "tags": "Categories"}

        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "add caption",
                    "class": "font1 text-4xl",
                },
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image_url"]
        labels = {"body": "Caption", "tags": "Categories"}

        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "add caption",
                    "class": "font1 text-4xl",
                },
            ),
            "tags": forms.CheckboxSelectMultiple(),
        }
