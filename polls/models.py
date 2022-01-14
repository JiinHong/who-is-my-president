import datetime

from django.db import models
from django.utils.datetime_safe import datetime
# Create your models her
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days='1')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # tendency 정치성향 (진보 P (progressive) 보수 C (conservative) 중도 M (midway)
    tendency = models.CharField(max_length=1, default="p", null=False, blank=False)


    def __str__(self):
        return self.choice_text