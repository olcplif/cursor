from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import AbstractUser
from src.apps.location.models import City


class CarDealerUsers(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=64,
        null=True,
        db_index=True,
        verbose_name="Title"
    )
    is_dealer = models.BooleanField(
        default=False
    )
    is_client = models.BooleanField(
        default=False
    )
    city_id = models.ForeignKey(
        to='location.City',
        on_delete=models.SET_NULL,
        null=True,
        related_name='users'
    )

    def __str__(self):
        return f'{self.pk}: {self.first_name} {self.last_name} ({self.title})'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in CarDealerUsers.objects.all():
        Token.objects.get_or_create(user=user)
