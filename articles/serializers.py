from rest_framework import serializers

from articles.models import Article


class ArticleSerializer( serializers.HyperlinkedModelSerializer ):
    #author = serializers.ReadOnlyField(source = 'author')
    category = serializers.ReadOnlyField(source = 'category.name')
   
    header_image = serializers.ImageField(use_url = True)
    


    class Meta:
        model = Article
        fields = [
                'id', 'title', 'creation_date', 
                'author', 'category', 'header_image',
                'body'
        ]
