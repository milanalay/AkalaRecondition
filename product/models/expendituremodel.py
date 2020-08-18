from django.db import models


# Create your models here.



class Expenditure(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    amount = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Amount')
    date = models.DateField(verbose_name='Date')


    def __str__(self):
        return self.name



