from django import forms
from .models import Math
class MathForm(forms.ModelForm):
    class Meta:
        model = Math
        fields = ['math1', 'math2', 'category']