from django import forms
from django.utils.translation import gettext_lazy as _

class ExampleForm(forms.Form):
    first_name = forms.CharField(label=_('first name'))


from django.forms import ModelForm
from .models import Contact, Comment


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')