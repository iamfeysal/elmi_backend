from django.contrib.auth import update_session_auth_hash, get_user_model
from rest_framework import serializers

from users.models import User, UserFeedback
from category.api.serializer import CategorySerializer, SubCategorySerializer


# from customers.api.serializer import FranchiseSerializer, B2bSerializer,\
#     EndSerializer


class UserFeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for working with the feedback model
    """

    class Meta:
        model = UserFeedback
        fields = ("user", "message", "date_submitted",
                  "message_polarity")


class UserSerializer(serializers.ModelSerializer):
    # userfeedback, = UserFeedbackSerializer()
    password = serializers.CharField(write_only=True, required=True)
    user_category = CategorySerializer(many=True)

    # confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            "id", "email", "password", "date_joined" , "last_login",
            'user_category')

        # read_only_fields = ('date_joined', "password", 'last_login',
        # 'userprofile') extra_kwargs = {'password' : {'write_only' : True,
        # 'required' : True}, }

        def create(self, validated_data):
            """ Create user using given validated fields """
            return User.objects._create_user(**validated_data)

        # def create(self, validated_data) :
        #     print('hit users serializer create function')
        #     """ Create user using given validated fields """
        #     # profile_data = validated_data.pop('profile')
        #     # password = validated_data.pop('password')
        #     # user = User(**validated_data)
        #     # user.set_password(password)
        #     # user.save()
        #     user = User.objects.create_user(**validated_data)
        #     return user

        def update(self, instance, validated_data):
            """ Update user details """
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
            update_session_auth_hash(self.context.get('request'), instance)
            return instance
            # instance.email = validated_data.get(
            #     'email', instance.email)
            # instance.save()
            # email = validated_data.get('email', None)
            # password = validated_data.get('password', None)
            # confirm_password = validated_data.get('confirm_password', None)
            # 
            # if password and confirm_password and password ==
            # confirm_password : instance.set_password(password)
            # instance.save() update_session_auth_hash(self.context.get(
            # 'request'), instance) return instance


class CreateUserSerializer(serializers.ModelSerializer):
    """
    User model without password
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'email', 'last_name',
                  'first_name', 'gender', 'contact_phone', 'is_staff',
                  'is_active', 'profile_picture', 'avatar')
