# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    city_id = models.AutoField(
        primary_key=True
    )
    city_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="City Name"
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.SET_NULL,
        db_column='country',
        blank=True,
        null=True,
        related_name='Country'
    )

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(
        primary_key=True
    )
    country_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Country Name"
    )
    abbreviation = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Short name"
    )

    class Meta:
        managed = False
        db_table = 'country'


class Dish(models.Model):
    dish_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Dish"
    )
    components = models.CharField(
        max_length=350,
        db_index=True,
        verbose_name="Components"
    )
    recipe = models.TextField()
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.SET_NULL,
        db_column='menu',
        blank=True,
        null=True,
        related_name='Menu'
    )

    class Meta:
        managed = False
        db_table = 'dish'


class Employee(models.Model):
    employee_id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Last Name"
    )
    position = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Position"
    )
    restaurant = models.ForeignKey(
        'Restaurant',
        db_column='restaurant',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        managed = False
        db_table = 'employee'


class Menu(models.Model):
    menu_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Menu Name"
    )
    for_season = models.ForeignKey(
        'Season',
        on_delete=models.SET_NULL,
        db_column='for_season',
        blank=True,
        null=True)
    restaurant = models.ForeignKey(
        'Restaurant',
        on_delete=models.SET_NULL,
        db_column='restaurant',
        blank=True,
        null=True
    )

    class Meta:
        managed = False
        db_table = 'menu'


class Restaurant(models.Model):
    restaurant_id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Restaurant Name"
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Restaurant Address"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        db_column='city',
        blank=True,
        null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Season(models.Model):
    season_id = models.AutoField(
        primary_key=True
    )
    season = models.CharField(
        max_length=10
    )

    class Meta:
        managed = False
        db_table = 'season'
