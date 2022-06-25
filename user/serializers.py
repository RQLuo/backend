from django.contrib.auth.models import User, Group
from rest_framework import serializers
from article.serializers import Article


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
        model = User
        fields = ('url', 'username', 'email', 'groups', 'articles')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')