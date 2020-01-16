from django.urls import path, re_path, include
from rest_framework import routers
from customers.api.serializer import B2bSerializer, FranchiseSerializer, \
    EndSerializer
from customers.api.views import B2bViewSet, FranchiseViewSet, EndViewSet

router = routers.DefaultRouter()
# router.register(r'b2bcusomer', B2bSerializer, basename='categories')
# router.register(r'franchisecustomer', FranchiseSerializer,
# basename='categories') router.register(r'endcustomer', EndSerializer,
# basename='categories')


urlpatterns = [
    # re_path('', include(router.urls)),
    re_path(r'^b2bcusomer$', B2bViewSet.as_view({'get': 'list'}),
            name='b2bcusomer'),
    re_path(r'^franchisecustomer$', FranchiseViewSet.as_view({'get': 'list'}),
            name='franchisecustomer'
            ),
    re_path(r'^endcustomer$', EndViewSet.as_view({'get': 'list'}),
            name='endcustomer'
            )

]