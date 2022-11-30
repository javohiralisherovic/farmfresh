from django import forms
from django.utils.translation import gettext_lazy as _

class ExampleForm(forms.Form):
    first_name = forms.CharField(label=_('first name'))


from django.forms import ModelForm
from .models import Contact, Comment


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-light border-0 px-4',
                'placeholder': 'Your Name',
                "type": "text",
                'style':"height: 55px;"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light border-0 px-4',
                'placeholder': 'Your Email',
                "type": "email",
                'style':"height: 55px;"
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control bg-light border-0 px-4',
                'placeholder': 'Your Subject',
                "type": "text",
                'style':"height: 55px;"
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-light border-0 px-4 py-3',
                'placeholder': 'Your Subject',
                'rows':"2" 
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-light border-0 px-4',
                'placeholder': 'Your Name',
                "type": "text",
                'style':"height: 55px;"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light border-0 px-4',
                'placeholder': 'Your Email',
                "type": "email",
                'style':"height: 55px;"
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control bg-light border-0 px-4 py-3',
                'placeholder': 'Your Comment',
                'rows':"2" 
            })
        }