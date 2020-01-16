from rest_framework import serializers
from customers.models import B2bCustomer, FranchiseCustomer, EndCustomer
from category.api.serializer import CategorySerializer
from users.api.serializers import UserSerializer


class B2bSerializer(serializers.ModelSerializer):
    """
    Serializer for working with the b2b customer model
    """
    category = CategorySerializer(allow_null=True)

    class Meta:
        model = B2bCustomer

        fields = '__all__'

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category')
        instance.save()

        return instance

    def updateuser(self, instance, validated_data):
        instance.borrower = validated_data.get('user')
        instance.save()

        return instance

    # def to_representation(self, instance):
    #     user = super(B2bSerializer, self).to_representation(instance)
    #     user['user'] = instance.user.full_name
    #     return user


class FranchiseSerializer(serializers.ModelSerializer):
    """
    Serializer for working with the franchise customer model
    """
    category = CategorySerializer(allow_null=True)
    user = UserSerializer()

    class Meta:
        model = FranchiseCustomer

        fields = '__all__'

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category')
        instance.save()

        return instance

    def updateuser(self, instance, validated_data):
        instance.user = validated_data.get('user')
        instance.save()

        return instance

    # def to_representation(self, instance):
    #     user = super(FranchiseSerializer, self).to_representation(instance)
    #     user['user'] = instance.user.full_name
    #     return user


class EndSerializer(serializers.ModelSerializer):
    """
    Serializer for working with the end customer model
    """
    category = CategorySerializer(allow_null=True)

    class Meta:
        model = EndCustomer

        fields = '__all__'

    def update(self, instance, validated_data):
        instance.borrower = validated_data.get('category')
        instance.save()

        return instance

    def to_representation(self, instance):
        user = super(EndSerializer, self).to_representation(instance)
        user['user'] = instance.user.full_name
        return user
