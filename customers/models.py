from django.db import models
from users.models import AUTH_USER_MODEL

from category.models import Category, SubCategory


# Create your models here.


class FranchiseCustomer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, blank=False, null=False,
                             on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return str(self.user)


# base class

class FranchiseSummary(FranchiseCustomer):
    class Meta:
        proxy = True
        verbose_name = "franchise sales summary"
        verbose_name_plural = "franchise summary"


class B2bCustomer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, blank=False, null=False,
                             on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return str(self.user)


class EndCustomer(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, blank=False, null=False,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return str(self.user)
