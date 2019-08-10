from rest_framework import serializers

from categories.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length = 50)

    articles = serializers.HyperlinkedRelatedField(many = True, view_name = 'article-list',
            read_only = True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'articles']
