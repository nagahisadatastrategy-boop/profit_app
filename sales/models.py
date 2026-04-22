from django.db import models

class Sales(models.Model):
    store_name = models.CharField(max_length=100)
    date = models.DateField()
    sales_amount = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.store_name} - {self.date}"