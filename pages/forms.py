from django import forms

from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Orden'}),
        }
        labels = {
            'title': '',
            'content': 'Contenido',
            'order': '',
        }
