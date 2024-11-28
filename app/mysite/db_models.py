from django.db import models


class UserInput(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    number3 = models.IntegerField()


class UserShopData(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()
    # gender = models.ChoiceField(choices=(('male', 'Мужской'), ('female', 'Женский')))
    address = models.CharField(max_length=100)
    subscription = models.BooleanField()