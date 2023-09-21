from django.db import models

# Create your models here.


class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()
    def __str__(self):
        return self.name
    
