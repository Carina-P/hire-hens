from django.db import models


class Faq(models.Model):
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.TextField(max_length=500, null=False, blank=False)
    objects = models.Manager()

    def __str__(self):
        return self.question
