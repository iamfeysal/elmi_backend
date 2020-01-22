from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework import routers

from users.api.views import UserFeedbackViewSet, UserView

router = routers.DefaultRouter()
router.register(r'feedback', UserFeedbackViewSet)
# router.register(r'users', UserView)
# router.register(r'devices', DeviceViewSet)
# router.register(r'messagetemplate', CreateMessageTemplateViewSet)
# router.register(r'mailalerts', MailAlertsViewSet)
# router.register(r'mailsubscription', MailSubscriptionViewSet)


# app_name = "authentication"


urlpatterns = [
    # path('sign_up', SignUp, name='sign_up'),
    # re_path('', include(router.urls)),
    re_path(r'^auth-token$', obtain_auth_token),
    re_path(r'^userlist$', UserView.as_view({'get': 'list'}))
]
