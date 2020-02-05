from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from category.api.serializer import CategorySerializer, SubCategorySerializer, \
    ActivesubsSerializer, ExpiredsubsSerializer
from category.models import Category, SubCategory


class CategoryViewSet(generics.ListCreateAPIView):
    """
    Lists categories with subcategory
    """

    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        This view should return a list of all the categories
        for the currently authenticated user.
        """
        user = self.request.user
        return Category.objects.filter(user_id=user, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class Categorywithnosubcategory(generics.ListCreateAPIView):
    """
    Lists categories with no subcategory
    """

    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        This view should return a list of all the categories
        for the currently authenticated user.
        """
        user = self.request.user
        return Category.objects.filter(user_id=user,
                                       category_subcategory=None)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class SubCategoryViewSet(generics.ListCreateAPIView):
    """
     class subcategory viewset
    """

    serializer_class = SubCategorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        This view should return a list of all the sub category id as a
        foreign key for the currently authenticated user.
        """
        user = self.request.user
        return SubCategory.objects.filter(user_id=user,
                                          category_id__isnull=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostSubcategory(APIView):
    # permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    serializer_class = SubCategorySerializer

    def post(self, request):
        # category = Category.objects.get(request.data['name'])
        # print(category)
        serializer = self.serializer_class(data=request.data, )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class Subcategorywithnocategory(generics.ListCreateAPIView):
#     """
#      class uncategorised viewset
#     """
#     serializer_class = SubCategorySerializer
#
# def get_queryset(self): """ This view should return a list of all the
# subcategory that does not have category id as a foreign key for the
# currently authenticated user. """ user = self.request.user return
# SubCategory.objects.filter(user_id=user, category_id__isnull=True)


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
