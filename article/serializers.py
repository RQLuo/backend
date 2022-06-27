from rest_framework import serializers
from article.models import Article
from user.serializers import UserSerializer
from article.models import Category
from article.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):

    @staticmethod
    def check_tag_obj_exists(validated_data):
        tag = validated_data.get('tag')
        if Tag.objects.filter(tag=tag).exists():
            raise serializers.ValidationError('Tag with text {} exists.'.format(tag))

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
        model = Category
        fields = '__all__'
        read_only_fields = ['url', 'create_date']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    # Create the entered tab if it does not exist
    def to_internal_value(self, data):
        tags_data = data.get('tag')
        if isinstance(tags_data, list):
            for tag in tags_data:
                if not Tag.objects.filter(tag=tag).exists():
                    Tag.objects.create(tag=tag)
        return super().to_internal_value(data)

    @staticmethod
    def validate_category(value):
        if not Category.objects.filter(category=value).exists():
            raise serializers.ValidationError("Category with text {} exists.".format(value))
        return value

    class Meta:
        tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
        model = Article
        fields = '__all__'
        read_only_fields = ('url', 'create_date', 'creator')
