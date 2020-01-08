from rest_framework import serializers
from users.models import User, UserFeedback, AUTH_USER_MODEL
from category.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for working with the category model
    """

    class Meta:
        model = Category

        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for working with the sub category model
    """
    class Meta:
        model = SubCategory

        fields = '__all__'

    def to_representation(self, instance):
        category = super(SubCategorySerializer, self).to_representation(
            instance)
        category['category'] = instance.category.name
        return category
