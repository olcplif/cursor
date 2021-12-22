from django.db import models

# Create your models here.
from src.common.models import SoftDeleteAuditModel
from src.apps.dealer.models import Dealer


class Car(SoftDeleteAuditModel):
    FUEL_PETROL = 'petrol'
    FUEL_DIESEL = 'diesel'
    FUEL_ELECTRIC = 'electric'
    FUEL_HYBRID = 'hybrid'

    FUEL_CHOICES = (
        (FUEL_PETROL, 'petrol'),
        (FUEL_DIESEL, 'diesel'),
        (FUEL_ELECTRIC, 'electric'),
        (FUEL_HYBRID, 'hybrid'),
    )

    POLLUTANT_CLASS_A_PLUS = 'A+'
    POLLUTANT_CLASS_A = 'A'
    POLLUTANT_CLASS_B = 'B'
    POLLUTANT_CLASS_C = 'C'
    POLLUTANT_CLASS_E = 'E'
    POLLUTANT_CLASS_F = 'F'
    POLLUTANT_CLASS_G = 'G'

    POLLUTANT_CLASS_CHOICES = (
        (POLLUTANT_CLASS_A_PLUS, 'A+'),
        (POLLUTANT_CLASS_A, 'A'),
        (POLLUTANT_CLASS_B, 'B'),
        (POLLUTANT_CLASS_C, 'C'),
        (POLLUTANT_CLASS_E, 'E'),
        (POLLUTANT_CLASS_F, 'F'),
        (POLLUTANT_CLASS_G, 'G'),
    )

    STATUS_IN_STOCK = 'in stock'
    STATUS_EXPECTED = 'expected'
    STATUS_ORDER = 'order'
    STATUS_DISCONTINUED = 'discontinued'

    STATUS_CHOICES = (
        (STATUS_IN_STOCK, 'in stock'),
        (STATUS_EXPECTED, 'expected'),
        (STATUS_ORDER, 'order'),
        (STATUS_DISCONTINUED, 'discontinued'),
    )

    GEAR_MECHANICAL = 'mechanical'
    GEAR_AUTOMATIC = 'automatic'

    GEAR_CHOICES = (
        (GEAR_MECHANICAL, 'mechanical'),
        (GEAR_AUTOMATIC, 'automatic'),
    )

    car_id = models.AutoField(primary_key=True)
    color_id = models.ForeignKey(
        to='Color',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    dealer_id = models.ForeignKey(
        to='dealer.Dealer',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    model_id = models.ForeignKey(
        to='Model',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    engine_type = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Engine type"
    )

    pollutant_class = models.CharField(
        max_length=25,
        choices=POLLUTANT_CLASS_CHOICES,
        default=POLLUTANT_CLASS_A_PLUS,
        blank=True
    )
    price = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Price"
    )
    fuel_type = models.CharField(
        max_length=25,
        choices=FUEL_CHOICES,
        default=FUEL_PETROL,
        blank=True,
        verbose_name="Fuel type"
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_IN_STOCK,
        blank=True,
        verbose_name="Status"
    )
    doors = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Doors"
    )
    capacity = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Capacity"
    )
    gear_case = models.CharField(
        max_length=25,
        choices=GEAR_CHOICES,
        default=GEAR_AUTOMATIC,
        blank=True,
        verbose_name="Gear case"
    )
    number = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Number"
    )
    slug = models.SlugField(
        max_length=40
    )
    sitting_place = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Sitting place"
    )
    first_registration_data = models.DateField()
    engine_power = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Engine power"
    )


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Color name"
    )


class Model(models.Model):
    color_id = models.AutoField(primary_key=True)
    brand_id = models.ForeignKey(
        to='Brand',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    name = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Model name"
    )


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Brand name"
    )


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    category = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Category name"
    )
    name = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Property name"
    )


class CarProperty(models.Model):
    car_property_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(
        to='Property',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
