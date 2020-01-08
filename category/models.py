from django.db import models


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
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
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
