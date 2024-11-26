from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


class PrimeNumbersForm(forms.Form):
    start = forms.IntegerField()
    stop = forms.IntegerField()


class UserShop(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=(('male', 'Мужской'), ('female', 'Женский')))
    address = forms.CharField()
    subscription = forms.BooleanField()