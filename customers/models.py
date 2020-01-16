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
