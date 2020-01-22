from django.urls import re_path
from rest_framework import routers

from category.api.views import CategoryViewSet, SubCategoryViewSet, \
    UncategoriedViewset, ActivesubViewset, ExipredsubViewset

router = routers.DefaultRouter()
# router.register(r'categories', CategorySerializer, basename='categories')
router.register(r'uncategorised_subs', UncategoriedViewset,
                basename='uncategorised_subs')

urlpatterns = [

    re_path(r'^category/$', CategoryViewSet.as_view(),
            name='category'),
    re_path(r'^sub_category/$', SubCategoryViewSet.as_view({'get': 'list'}),
            name='sub_category'
            ),
    re_path(r'^uncategorised_subs/$',
            UncategoriedViewset.as_view(),
            name='uncategorised_subs'
            ),
    re_path(r'^activesubs/$',
            ActivesubViewset.as_view(),
            name='activesubs'
            ),
    re_path(r'^expiredsubs/$',
            ExipredsubViewset.as_view(),
            name='expiredsubs'
            )

]
