from django import forms
from .models import Join

class CollectEmailForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ['full_name', 'email']