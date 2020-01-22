from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from users.api.serializers import UserFeedbackSerializer, UserSerializer
from users.models import User, UserFeedback


class UserView(viewsets.ModelViewSet):
    """
    Lists users
    """

    # queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserFeedbackViewSet(viewsets.ModelViewSet):
    """
    Lists user feedbacks
    """

    queryset = UserFeedback.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserFeedbackSerializer
