from django.db import models



class Incoming(models.Model):
    availability = (
        ('Available', 'Available'),
        ('Sold', 'Sold'),
    )
    model = (
        ('2020', '2020'),
        ('2019', '2019'),
        ('2018', '2018'),
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
        ('2014', '2014'),
        ('2013', '2013'),
        ('2012', '2012'),
        ('2011', '2011'),
        ('2010', '2010'),
    )
    name = models.CharField(max_length=200, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    image = models.FileField(upload_to="images/", blank=True)
    model = models.CharField(max_length=200, choices=model, verbose_name='Model')
    bike_number = models.CharField(max_length=200, verbose_name='Bike Number')
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Buy Price')
    sale_price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Sale Price')
    owner = models.CharField(max_length=200, verbose_name='Owner')
    contact = models.BigIntegerField(verbose_name='Contact', blank=True)
    stock = models.CharField(max_length=200, choices=availability, default='Available', verbose_name='In Stock')
    sanakhat = models.BooleanField(default=False, verbose_name='Sanakhat')
    passed = models.BooleanField(default=False, verbose_name='Passed')
    date = models.DateField(verbose_name='Date')
    


    def __str__(self):
        return self.name



class Outgoing(models.Model):
    product = models.OneToOneField(Incoming, on_delete=models.CASCADE, verbose_name='Incoming', related_name='outgoing_product')
    price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Sale Price')
    customer = models.CharField(max_length=200, verbose_name='Customer')
    contact = models.BigIntegerField(verbose_name='Contact', blank=True)
    date = models.DateField(verbose_name='Date')
    
    def __str__(self):
        return self.product.name
    
    
    def calc_profit(self):
        data1 = self.price
        data2 = self.product.price
        data = (data1 - data2)
        return data

