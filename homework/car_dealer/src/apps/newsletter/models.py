from django.db import models


# Create your models here.
class NewsLetter(models.Model):
    newsletter_id = models.AutoField(primary_key=True)
    email = models.EmailField(
        blank=True,
        verbose_name="email address"
    )
