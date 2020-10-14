from django.forms import ModelForm, RadioSelect

from .models import *


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(placeholder='Ваше имя')
        self.fields['email'].widget.attrs.update(placeholder='e-maill (не обязательно)')
        self.fields['phone'].widget.attrs.update(placeholder='номер телефона')

    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'category': RadioSelect(),
            'subcategory': RadioSelect(),
        }
