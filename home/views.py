from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from users.models import User, UserFeedback, AUTH_USER_MODEL
from category.models import Category, SubCategory
from customers.models import FranchiseCustomer, B2bCustomer, EndCustomer
from decimal import Decimal


# @login_required()
def index(request):
    franchise_customers = FranchiseCustomer.objects.all()
    franchise_count = franchise_customers.count()

    b2b_customers = B2bCustomer.objects.all()
    b2b_count = b2b_customers.count()

    end_customers = EndCustomer.objects.all()
    end_customers_count = end_customers.count()

    subcategory = SubCategory.objects.all()
    print(subcategory)
    my_list = []
    for data in subcategory:
        year = 12
        start_date = data.start_date
        end_date = data.end_date
        diff = (end_date - start_date).days
        price = data.price
        total_year = diff * price * year
        # my_list.append(total_year)
        b = sum(my_list)
        print(b)

        # sum_numbers += total_year
        # print(sum_numbers)
        # total_year = sum(int(diff) * int(price) * int(year))

    # start_date = SubCategory.start_date
    # print(start_date)
    # end_date = (SubCategory.end_date)
    # print(end_date)
    # diff = (end_date - start_date).days
    # print(diff)
    # total_subscription_eran = diff * SubCategory.price

    return render(request, 'admin/index.html', {
        'franchise_count': franchise_count, 'b2b_count': b2b_count,
        'end_customers_count': end_customers_count})
