from users.models import PersonalUser

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile_photo = serializers.ImageField(max_length = 100, use_url = True)
    personal_info = serializers.CharField(max_length =200, allow_blank = True )
    
    articles = serializers.HyperlinkedRelatedField(many = True, view_name = 'article-detail',
            read_only = True)

    class Meta:
        model = PersonalUser
        fields = ['id', 'username', 'email',
                  'profile_photo', 'articles', 'personal_info']
