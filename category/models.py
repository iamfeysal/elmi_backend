import datetime

from django.db import models
from decimal import Decimal


# Create your models here.


class Category(models.Model):
    # parent = models.ForeignKey('self', on_delete=models.CASCADE)  # Here
    # category # will # refer to it # self
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True,
                            help_text='subcategory name')
    monitor_name = models.CharField(max_length=255, blank=True, null=True,
                                    help_text='monitor name')
    start_date = models.DateField()
    end_date = models.DateField()
    subscription_type = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                help_text='price per month')
    playbox_price = models.DecimalField(max_digits=10, decimal_places=2)
    support_contract = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    extra_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.monitor_name) + ": $" + str(self.price)

    # def returntotal(self):
    #     """
    #     :return total price
    #     """
    #     # date = (self.start_date - self.end_date)
    #     # date_diffrence = date.days
    #     diff = abs((self.end_date - self.start_date))
    #     print('date difference is-----:', diff)
    #     price = self.price
    #     print('PRICE IS------------:',  price)
    #     return price * diff

    def totalsubscritionearn(self):
        """
        :return total price of subscription
        """
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        print(diff)
        total = diff * self.price
        print(total)
        print('difference is----', diff)
        return total

    def totalplayboxearn(self):
        """
        :return total playbox earning
        """
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        print(diff)
        total = diff * self.playbox_price
        print(total)
        print('difference is----', diff)
        return total

    def totalsupportearning(self):
        """
        :return total price
        """
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        print(diff)
        total = diff * self.support_contract
        print(total)
        print('difference is----', diff)
        return total
