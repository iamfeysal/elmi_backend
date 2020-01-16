from rest_framework import viewsets

from category.api.serializer import CategorySerializer, SubCategorySerializer
from category.models import Category, SubCategory


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Lists categories
    """

    queryset = Category.objects.all()
    print('categories are:', queryset.count())
    # permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    Lists all subcategories
    """

    queryset = SubCategory.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = SubCategorySerializer
