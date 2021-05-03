from django.db import models
from datetime import datetime, timezone

class myMod(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(max_length=2056, null=False, blank=False)
    image = models.ImageField(upload_to='media', null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=False, verbose_name="date_published", default=datetime.now)
    person = models.ForeignKey('auth.User', related_name='myMod', default=None, on_delete=models.CASCADE)





