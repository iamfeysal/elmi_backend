from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import AUTH_USER_MODEL
from django.conf import settings


# Create your models here.


class Category(models.Model):
    # parent = models.ForeignKey('self', on_delete=models.CASCADE)  # Here
    # category # will # refer to it # self
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_category')

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                             blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='category_subcategory')
    name = models.CharField(max_length=255, blank=True, null=True,
                            help_text='subcategory name')
    in_progress = models.BooleanField(default=True, help_text='licensed '
                                                              'active',
                                      blank=True, null=True)
    monitor_name = models.CharField(max_length=255, blank=True, null=True,
                                    help_text='monitor name')
    start_date = models.DateField()
    end_date = models.DateField()
    subscription_type = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, blank=True, null=True,
                                decimal_places=2,help_text='price per month')
    playbox_price = models.DecimalField(max_digits=10, decimal_places=2,
                                        blank=True, null=True)
    support_contract = models.DecimalField(max_digits=10, decimal_places=2,
                                           blank=True, null=True)
    email = models.EmailField(verbose_name="email", max_length=60, null=True,
                              blank=True)
    extra_income = models.DecimalField(max_digits=10, decimal_places=2,
                                       blank=True, null=True)

    def __str__(self):
        return str(self.monitor_name) + ": $" + str(self.price)

    # def expired(self):
    #     start_date = (self.start_date)
    #     end_date = (self.end_date)
    #     first = 0
    #     diff = ((end_date - start_date).days + 1)
    #     # print(diff)
    #     return first + 1 if diff <= 0 else 0

    # def active(self):
    #     start_date = (self.start_date)
    #     end_date = (self.end_date)
    #     first = 0
    #     diff = ((end_date - start_date).days + 1)
    #     # print(diff)
    #     return first + 1 if diff <= 0 else 0
    # if diff <= 0:
    #     return True

    def totalsubscritionearn(self):
        """
        :return total price of subscription
        """
        if SubCategory is not None:
            start_date = (self.start_date)
            end_date = (self.end_date)
            diff = ((end_date - start_date).days)
            total = diff * self.price
            return total
        else:
            return None

    def totalplayboxearn(self):
        """
        :return total playbox earning
        """
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        total = diff * self.playbox_price
        return total

    def totalsupportearning(self):
        """
        :return total price
        """
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        total = diff * self.support_contract
        return total

    @transaction.atomic
    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):
        print('hit save method')
        start_date = (self.start_date)
        end_date = (self.end_date)
        diff = ((end_date - start_date).days)
        print(diff)
        if diff <= 0:
            self.in_progress = False
            print(self.in_progress)
        super(SubCategory, self).save(force_insert=force_insert,
                                      force_update=force_update, using=using,
                                      update_fields=update_fields)
