from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'articles_img']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва статті'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статті'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публікації'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статті'
            }),
            "articles_img": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Виберіть зображення'
            })

        }
