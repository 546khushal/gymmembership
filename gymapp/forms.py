from django import forms
from .models import registerm

class RegistermForm(forms.ModelForm):
    class Meta:
        model = registerm
        fields = '__all__' 