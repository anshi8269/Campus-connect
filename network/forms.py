from django import forms
from .models import FacebookPage

class FacebookPageForm(forms.ModelForm):
    class Meta:
        model = FacebookPage
        fields = ['name', 'category', 'description', 'image']