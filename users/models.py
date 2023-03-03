from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    age = models.IntegerField()

    class Sex(models.TextChoices):
        MALE = 'ML'
        FEMALE = 'FM'
        UNDECIDED = 'UD'

    sex = models.CharField(max_length=2, choices=Sex.choices, default=Sex.UNDECIDED)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


