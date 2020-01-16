from django.urls import path, re_path
from rest_framework import routers
from category.api.serializer import CategorySerializer
from category.api.views import CategoryViewSet, SubCategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategorySerializer, basename='categories')
# router.register(r'sub_categories', SubCategorySerializer,
#                 basename='sub_categories')

urlpatterns = [

    re_path(r'^category$', CategoryViewSet.as_view({'get': 'list'}),
            name='category'),
    re_path(r'^sub_category$', SubCategoryViewSet.as_view({'get': 'list'}),
            name='sub_category'
            )

]
