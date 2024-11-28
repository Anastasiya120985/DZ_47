from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


class CalculationForm(forms.Form):
    number1 = forms.IntegerField(label='Число 1')
    number2 = forms.IntegerField(label='Число 2')
    number3 = forms.IntegerField(label='Число 3')
    choices = [('min', 'Минимум'), ('max', 'Максимум'), ('avg', 'Среднеарифметическое')]
    operation = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)


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