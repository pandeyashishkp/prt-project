from django import forms
from .models import Hpux


class HpuxForm(forms.ModelForm):
    servername = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    patch_bundle = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Hpux
        fields = ['servername', 'email', 'patch_bundle', 'date', ]
