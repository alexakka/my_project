from django.db import models
from django.utils import timezone
from users.models import User


# Create your models here.
class Survey(models.Model):
    survey_name = models.CharField(max_length=200)
    description = models.TextField()
    added_time = models.TimeField(auto_now_add=timezone.now())
    published_time = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.survey_name


class Question(models.Model):
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text





