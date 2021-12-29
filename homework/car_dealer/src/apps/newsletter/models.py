from django.db import models


# Create your models here.
class NewsLetter(models.Model):
    email = models.EmailField(
        blank=True,
        verbose_name="email address"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
