from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# from src.common.models import BaseDateAuditModel, SoftDeleteAuditModel


class Dealer(AbstractUser):
    dealer_id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Title"
    )
    city_id = models.ForeignKey(
        to='City',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cities'
    )

    def __str__(self):
        return f'{self.pk}: {self.first_name} {self.last_name} ({self.title})'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name="City Name"
    )
    country_id = models.ForeignKey(
        to='Country',
        on_delete=models.SET_NULL,
        null=True,
        related_name='countries'
    )


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name="Country Name"
    )
    code = models.CharField(
        max_length=10,
        db_index=True,
        verbose_name="Country code"
    )
