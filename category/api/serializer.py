from rest_framework import serializers

from category.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for working with the sub category model
    """
    totalsubscritionearn = serializers.CharField()
    totalplayboxearn = serializers.CharField()
    totalsupportearning = serializers.CharField()

    class Meta:
        model = SubCategory

        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.category = validated_data.get('category')
    #     instance.save()
    #     return instance


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for working with the category model
    """
    subcategory = SubCategorySerializer(source='category_subcategory',
                                        many=True)

    # print(subcategory)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategory')


class UncategorisedsubSerializer(serializers.Serializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ActivesubsSerializer(serializers.Serializer):
    # category = CategorySerializer()
    # subcategory = SubCategorySerializer
    active = serializers.SerializerMethodField('get_in_progress')

    def get_in_progress(self, category):
        qs = SubCategory.objects.filter(in_progress=True)
        print(qs)
        serializer = SubCategorySerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = SubCategory
        fields = '__all__'


class ExpiredsubsSerializer(serializers.Serializer):
    # expired = serializers.CharField()

    active = serializers.SerializerMethodField('get_in_progress')

    def get_in_progress(self, category):
        qs = SubCategory.objects.filter(in_progress=False)
        print(qs)
        serializer = SubCategorySerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = SubCategory
        fields = '__all__'
