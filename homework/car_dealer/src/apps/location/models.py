from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name="City Name"
    )
    country_id = models.ForeignKey(
        to='Country',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cities'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Country(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
