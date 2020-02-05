from django.urls import re_path
from rest_framework import routers

from category.api.views import CategoryViewSet, SubCategoryViewSet, \
    UncategoriedViewset, ActivesubViewset, ExipredsubViewset, \
    Categorywithnosubcategory, PostSubcategory
router = routers.DefaultRouter()
# router.register(r'categories', CategorySerializer, basename='categories')
router.register(r'uncategorised_subs', UncategoriedViewset,
                basename='uncategorised_subs')

urlpatterns = [

    re_path(r'^category/$', CategoryViewSet.as_view(),
            name='category'),
    re_path(r'^catwithnosub/$', Categorywithnosubcategory.as_view(),
            name='catwithnosub'),
    re_path(r'^sub_category/$', SubCategoryViewSet.as_view(),
            name='sub_category'
            ),
    re_path(r'^post_sub_category/$', PostSubcategory.as_view(),
            name='post_sub_category'
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
