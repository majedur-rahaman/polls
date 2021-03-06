import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200,default="")
    pub_date = models.DateTimeField('date published')

    @python_2_unicode_compatible
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,default=0)
    choice_text = models.CharField(max_length=200,default="")
    votes = models.IntegerField(default=0)

    @python_2_unicode_compatible
    def __str__(self):
        return self.choice_text



