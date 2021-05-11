from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class myMod(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(max_length=2056, null=False, blank=False)
    image = models.ImageField(upload_to='media', null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=False, verbose_name="date_published", default=datetime.now)
    person = models.ForeignKey('auth.User', related_name='myMod', default=None, on_delete=models.CASCADE)





