# Register your models here.
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from authentications.forms import UserChangeForm, UserCreationForm
from category.models import Category, SubCategory
from customers.models import FranchiseCustomer, B2bCustomer, EndCustomer
from users.models import User, UserFeedback

admin.site.site_header = " ELMI SYSTEM Admin"
admin.site.site_title = " ELMI SYSTEM Admin Portal"
admin.site.index_title = "Welcome to ELMI SYSTEM Portal"


class MyUserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ('username', "email", 'avatar', "first_name",
                    "last_name",)  #
    # Contain
    # only
    # fields in your
    # `custom-user-model`
    list_filter = (
        'last_login', 'date_joined',)  # Contain only fields in your #
    # `custom-user-model` intended for filtering. Do not include
    # `groups`since you do not have it search_fields = ('is_player',
    # 'is_player',)  # Contain only fields in your `custom-user-model`
    # intended for searching ordering = ('is_player', 'is_coach',)  # Contain
    # only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()  # Leave it empty. You have neither `groups` or

    readonly_fields = ['date_joined', 'last_login', ]

    fieldsets = (
        (_('Personal info'),
         {'fields': ('email', "first_name", "last_name", "username",
                     'password',
                     )}),
        (_('Permissions'), {'fields': ('is_admin', 'is_staff',
                                       'is_superuser', 'is_active'), }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # (_('Relationship'), {'fields': ('followers', 'following')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name',
                       'last_name',)}
         ),
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

    # user_info.short_description = 'Category name'

    def get_queryset(self, request):
        queryset = super(CategoryAdmin, self).get_queryset(request)
        queryset = queryset.order_by('name', 'user')
        return queryset


# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('category', 'name', 'monitor_name', 'start_date',
#                     'end_date', 'subscription_type', 'condition', 'price',
#                     'playbox_price', 'support_contract', 'email', 'extra_income'
#                     )
#
#     def user_info(self, obj):
#         return obj
#
#     # user_info.short_description = 'Category name'
#
#     def get_queryset(self, request):
#         queryset = super(SubCategoryAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('name')
#         return queryset


class FranchiseAdmin(admin.ModelAdmin):

    list_display = ('user', "category", "franchise_count")

    change_list_template = 'admin/franchise_change_list.html'

    # date_hierarchy = 'published_date'

    def franchise_count(self, request):
        return FranchiseCustomer.objects.all().count()


admin.site.register(User, MyUserAdmin, )
admin.site.register(UserFeedback)
admin.site.register(FranchiseCustomer, FranchiseAdmin)
admin.site.register(B2bCustomer)
admin.site.register(EndCustomer)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)
admin.site.register(SubCategory)
