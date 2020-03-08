from django.db import models
from django.utils import timezone

# Create your models here.
class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
