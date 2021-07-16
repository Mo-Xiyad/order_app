from django.db import models
import random
from decimal import Decimal


class BouquetType(models.Model):
    bouquet_type = models.CharField(max_length=100)

    def __str__(self):
        return self.bouquet_type


class Product(models.Model):
    product_id = models.IntegerField(max_length=4, null=True, blank=True)
    title = models.CharField(max_length=220)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __int__(self):
        return self.product_id


class Order(models.Model):
    SIZE = (
        ('SMALL', 'Small',),
        ('MEDIUM', 'Medium',),
        ('LARGE', 'Large',),
    )
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField(default='', help_text='Contact phone number', blank=False, )
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE)
    quantity = models.IntegerField()
    bouquet_type = models.ForeignKey(BouquetType, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)  # automatically datetime object


    # def calculate(self, save=False):
    #     if not self.product:
    #         return {}
    #     subtotal = self.product.price
    #     shipping_fee = Decimal(55.00)
    #     total = subtotal + shipping_fee
    #     totals = {
    #         "subtotal": subtotal,
    #         "shipping_fee": shipping_fee,
    #         "total": total
    #     }
    #     for k, v in totals.items():
    #         setattr(self, k, v)
    #         if save == True:
    #             self.save()  # obj.save()
    #     return totals

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.date = timezone.now()
    #     return super(Flower, self).save(*args, **kwargs)
    #     self.updated_at = timezone.now()

    # def save(self, *args, **kwargs):
        # timedelt = datetime.timedelta()
        # self.updated_at = default=self.start_datetime + timedelta(hours=self.z)
    #     # self.updated_at = self.date
    #     # self.return_date = datetime.now()
    #     # time = self.return_date.time()
    #     # self.date = str(date), time.strftime("%H:%M:%S")
    #     # if self.date:
    #     #     self.date = self.start_datetime
    #     # self.date = datetime.now()
    #     # self.date = self.date.strftime("%m/%d/%Y"), time.strftime("%H:%M:%S")
    #     return super(Flower, self).save(*args, **kwargs)






