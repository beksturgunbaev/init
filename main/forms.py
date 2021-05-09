from .models import Feed
from django.forms import ModelForm, TextInput

class feedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['feedName', 'feedPhone', 'feedEmail']

        widgets = {
            'feedName': TextInput(attrs={
                'class': 'modal--input',
                'placeholder': 'Введите ваше имя',
                'type': 'text'
            }),
            'feedPhone': TextInput(attrs={
                'class': 'modal--input',
                'placeholder': 'Введите ваш телефон',
                'type': 'tel'
            }),
            'feedEmail': TextInput(attrs={
                'class': 'modal--input',
                'placeholder': 'Введите ваш email',
                'type': 'email'
            })
        }