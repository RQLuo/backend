from rest_framework import serializers
from article.models import Article
from user.serializers import UserSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('url', 'create_date', 'creator')
