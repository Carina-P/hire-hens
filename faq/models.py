from django.db import models

# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.question
