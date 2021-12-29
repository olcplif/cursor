from django.db import models

from src.common.models import SoftDeleteAuditModel
from src.apps.cars.models import Car


class Picture(SoftDeleteAuditModel):
    url = models.FileField(
        upload_to='static/images/cars/%Y/%m/%d/',
        null=True,
        blank=True,
    )
    car_id = models.ForeignKey(
        to='cars.Car',
        on_delete=models.SET_NULL,
        null=True,
        related_name='pictures'
    )
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
