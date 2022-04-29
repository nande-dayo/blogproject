import imp
from sre_constants import CATEGORY
from statistics import mode
from unicodedata import category
from certifi import contents
from django.db import models
from numpy import number
from django.db import models

class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('business','ビシネス'),('life','生活'),('other','その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices= CATEGORY

    )
    def __str__(self):
        return self.title
