from django import forms
from .models import Hpux


class HpuxForm(forms.ModelForm):
    class Meta:
        model = Hpux
        fields = [
            'servername',
            'email',
            'date',
            'patch_bundle'
        ]
