import self as self
from django import forms
from .models import *
from .views import *


class OrderItemCreateForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1)


class ProductParameterForm(forms.Form):
    parameter = forms.ChoiceField()


def get_parameter(prod_slug):
    qs = ProductParameter.objects.filter(product_info__product__slug=prod_slug)
    # param = qs
    choice = [[ind, item.__str__()] for ind, item in enumerate(qs)]
    # print(choice)
    form = ProductParameterForm()
    form.fields['parameter'].choices = choice
    # form.fields['parameter'].choices = param

    return form


class UserCreationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



