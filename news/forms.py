from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category_post', 'name_post', 'text_post', 'author_post']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name_post')
        text = cleaned_data.get('text_post')
        if title == text:
            raise ValidationError(
                "Название не должно совпадать с текстом"
            )
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category_post', 'name_post', 'text_post', 'author_post']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('name_post')
        text = cleaned_data.get('text_post')
        if title == text:
            raise ValidationError(
                "Название не должно совпадать с текстом"
            )
        return cleaned_data






