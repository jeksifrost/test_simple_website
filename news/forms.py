from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article name'
            }),
            'announcement': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            })
        }