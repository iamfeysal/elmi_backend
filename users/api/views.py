from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import users
from users.api.serializers import  UserFeedbackSerializer, UserSerializer
from users.models import User, UserFeedback

# 
# class ListUsersView(viewsets.ModelViewSet):
#     
#     # print('hit list user view')
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     # # permission_classes = (IsAuthenticated,)
# 
#     def post(self, request, format=None) :
#         
#         print('hit user post-------------------------')
#         serializer = self.serializer_class(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             print(serializer.is_valid())
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class UserViewSet(viewsets.ModelViewSet):
#     """User ViewSet.
#
#     get:
#     List all users
#
#     put:
#     Create new user with the given validated data
#
#     """
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#
#
#     def create(self, request):
#         print('hit create view')
#         """
#         Create user with validated data from the serializer class
#         """
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             print(serializer.is_valid)
#             User.objects._create_user(**serializer.validated_data)
#             return Response(serializer.validated_data,
#                             status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserFeedbackViewSet(viewsets.ModelViewSet) :
    """
    Lists user feedbacks
    """

    queryset = UserFeedback.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserFeedbackSerializer
