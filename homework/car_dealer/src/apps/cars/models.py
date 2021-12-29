from django.db import models

from src.apps.users.models import CarDealerUsers
from src.common.models import SoftDeleteAuditModel


class Car(SoftDeleteAuditModel):
    car = models.AutoField(primary_key=True)
    color = models.ForeignKey(
        to='Color',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    dealer = models.ForeignKey(
        to='users.CarDealerUsers',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    model = models.ForeignKey(
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
    fuel_type = models.CharField(
        max_length=25,
        choices=FUEL_CHOICES,
        default=FUEL_PETROL,
        blank=True,
        verbose_name="Fuel type"
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

    GEAR_MECHANICAL = 'mechanical'
    GEAR_AUTOMATIC = 'automatic'

    GEAR_CHOICES = (
        (GEAR_MECHANICAL, 'mechanical'),
        (GEAR_AUTOMATIC, 'automatic'),
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

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Color(models.Model):
    color = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=15,
        db_index=True,
        verbose_name="Color name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Model(models.Model):
    model = models.AutoField(primary_key=True)
    brand = models.ForeignKey(
        to='Brand',
        on_delete=models.SET_NULL,
        null=True,
        related_name='models'
    )
    name = models.CharField(
        max_length=15,
        db_index=True,
        unique=True,
        verbose_name="Model name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Brand(models.Model):
    brand = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=15,
        db_index=True,
        unique=True,
        verbose_name="Brand name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Property(models.Model):
    property = models.AutoField(primary_key=True)
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

    def __str__(self):
        return self.name


class CarProperty(models.Model):
    car_property = models.AutoField(primary_key=True)
    property = models.ManyToManyField(
        to='Property',
        null=True,
        related_name='cars'
    )
    car = models.ManyToManyField(
        to='Car',
        null=True,
        related_name='car_properties'
    )

    def __str__(self):
        return f"Car's properties"
