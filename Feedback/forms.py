from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    model = FeedBack
    fields = ['name', 'phone', 'email']