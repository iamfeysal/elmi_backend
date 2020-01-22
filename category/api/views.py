from rest_framework import generics
from rest_framework import viewsets

from category.api.serializer import CategorySerializer, SubCategorySerializer, \
    ActivesubsSerializer, ExpiredsubsSerializer
from category.models import Category, SubCategory


class CategoryViewSet(generics.ListCreateAPIView):
    """
    Lists categories
    """

    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the categories
        for the currently authenticated user.
        """
        user = self.request.user
        return Category.objects.filter(user_id=user)


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
     class subcategory viewset
    """

    serializer_class = SubCategorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the sub category id as a
        foreign key for the currently authenticated user.
        """
        user = self.request.user
        return SubCategory.objects.filter(user_id=user,
                                          category_id__isnull=False)


class UncategoriedViewset(generics.ListCreateAPIView):
    """
     class uncategorised viewset
    """
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        """
        This view should return a list of all the subcategory that does not have
        category id as a foreign key for the currently authenticated user.
        """
        user = self.request.user
        return SubCategory.objects.filter(user_id=user,
                                          category_id__isnull=True)


class ActivesubViewset(generics.ListAPIView):
    """
         class active subcategory viewset

    """
    serializer_class = ActivesubsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the active sub category
        for the currently authenticated user.
        """
        user = self.request.user
        return SubCategory.objects.filter(user_id=user, in_progress=True)


class ExipredsubViewset(generics.ListAPIView):

    """
         class expired subcategories viewset

    """
    serializer_class = ExpiredsubsSerializer

    def get_queryset(self):
        """
        This view should return a list of all expired sub cutegory
        for the currently authenticated user.
        """
        user = self.request.user
        return SubCategory.objects.filter(user_id=user, in_progress=False)


