from rest_framework import serializers

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
    totalsubscritionearn = serializers.CharField()
    totalplayboxearn = serializers.CharField()
    totalsupportearning = serializers.CharField()
    category = CategorySerializer()

    class Meta:
        model = SubCategory

        fields = '__all__'

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category')
        instance.save()

        return instance

    # def to_representation(self, instance):
    #     " get foreign key field"
    #     category = super(SubCategorySerializer, self).to_representation(
    #         instance)
    #     category['category'] = instance.category.name
    #     return category
