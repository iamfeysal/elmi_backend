from rest_framework import serializers

from category.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for working with the sub category model
    """
    totalsubscritionearn = serializers.CharField(read_only=True, required=False)
    totalplayboxearn = serializers.CharField(read_only=True, required=False)
    totalsupportearning = serializers.CharField(read_only=True, required=False)
    in_progress = serializers.CharField(read_only=True, required=False)

    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SubCategory

        fields = '__all__'

    def create(self, validated_data):
        return SubCategory.objects.create(**validated_data)


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

    def to_representation(self, instance):
        rep = super(CategorySerializer, self).to_representation(instance)
        rep['category'] = instance.name
        return rep


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
