from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=200)
    expiration_date = models.DateField(blank=True)
    is_day_before = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['expiration_date']
