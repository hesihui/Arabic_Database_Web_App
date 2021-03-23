from rest_framework import serializers
from articles.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        # TODO: improve the styling of the following line
        fields = ('id',
                  'title',
                  'content',
                  'authors',
                  'year',
                  'form',
                  'language',
                  'tags'
                  )
