from django.db import models


# Create your models here.

class Order(models.Model):

    STATUS_FORMED = 'formed'
    STATUS_WAITING_PAYMENT = 'waiting for payment'
    STATUS_PAID = 'paid'
    STATUS_DELIVERED = 'delivered'
    STATUS_COMPLETED = 'completed'
    STATUS_RETURN = 'return'

    STATUS_CHOICES = (
        (STATUS_FORMED, 'formed'),
        (STATUS_WAITING_PAYMENT, 'waiting for payment'),
        (STATUS_PAID, 'paid'),
        (STATUS_DELIVERED, 'delivered'),
        (STATUS_COMPLETED, 'completed'),
        (STATUS_RETURN, 'return'),
    )

    order_id = models.AutoField(primary_key=True)
    car_id = models.ForeignKey(
        to='car.Car',
        on_delete=models.SET_NULL,
        null=True,
        related_name='cars'
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_FORMED,
        blank=True,
        verbose_name="Status"
    )
    first_name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="First name"
    )
    last_name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Last name"
    )
    email = models.EmailField(
        blank=True,
        verbose_name="email address"
    )
    phone = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Phone"
    )
    message = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name="Message"
    )

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
