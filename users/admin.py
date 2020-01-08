from django.contrib import admin

# Register your models here.
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from authentications.forms import UserChangeForm, UserCreationForm
from users.models import User, UserFeedback
from category.models import Category, SubCategory
from customers.models import FranchiseCustomer, B2bCustomer, EndCustomer
from django.contrib import admin
from django.contrib.auth.models import Group


class UserFeedbackInline(admin.StackedInline):
    model = UserFeedback


class FranchiseInline(admin.StackedInline):
    model = FranchiseCustomer


class B2bInline(admin.StackedInline):
    model = B2bCustomer


class EndInline(admin.StackedInline):
    model = EndCustomer


class CategoryInline(admin.StackedInline):
    model = Category


class MyUserAdmin(auth_admin.UserAdmin):

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MyUserAdmin, self).get_inline_instances(request, obj)

    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ('email', 'avatar', "first_name", "last_name", "username",
                    'date_joined', 'is_admin', 'is_active',
                    'is_staff', 'is_superuser', 'last_login')  #
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
    # `user_permissions`
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields' : ('mobile',)}),
    # )
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

    inlines = [UserFeedbackInline, FranchiseInline,]

    # disable change of email if user is not superuser
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'email',
                'is_superuser',
                'user_permissions',
            }
        # Prevent non-superusers from editing their own permissions
        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    def has_delete_permission(self, request, obj=None):
        """
        # prevent staff users from deleting a model instance, regardless of
        their permissions
        """
        return False

    actions = [
        'activate_users',
    ]

    def activate_users(self, request, queryset):
        """
        handy admin action to mark multiple users as active Using this
        action, a staff user can mark one or more users, and activate them
        all at once. This is useful in all sorts of cases, such as if you had
        a bug in the registration process and needed to activate users in bulk
        """
        assert request.user.has_perm('auth.change_user')
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))

    activate_users.short_description = 'Activate Users'  # type: ignore

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            """
            hide activate_users() from users without change permission, 
            override get_actions()
            """
            del actions['activate_users']
        return actions


# admin.site.unregister(User)
admin.site.register(User, MyUserAdmin, )
admin.site.register(UserFeedback)
admin.site.register(FranchiseCustomer)
admin.site.register(B2bCustomer)
admin.site.register(EndCustomer)
admin.site.register(Category)
admin.site.unregister(Group)
admin.site.register(SubCategory)
