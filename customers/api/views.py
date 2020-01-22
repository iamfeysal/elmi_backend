from rest_framework import viewsets
from customers.api.serializer import B2bSerializer, FranchiseSerializer, \
    EndSerializer
from customers.models import B2bCustomer, FranchiseCustomer, EndCustomer


class B2bViewSet(viewsets.ModelViewSet):
    """
    Lists categories
    """

    queryset = B2bCustomer.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = B2bSerializer


class FranchiseViewSet(viewsets.ModelViewSet):
    """
    Lists categories
    """

    queryset = FranchiseCustomer.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = FranchiseSerializer


class EndViewSet(viewsets.ModelViewSet):
    """
    Lists categories
    """

    queryset = EndCustomer.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = EndSerializer
