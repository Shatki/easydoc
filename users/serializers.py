from rest_framework import serializers
from users.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
    #photo = serializers.FilePathField(path='tmp')
    class Meta:
        model = User
        fields = ('name',
                  'username',
                  'email',
                  'first_name',
                  'last_name',
                  'tag_line',
                  'photo',
                  'phone',
                  'photo',
                  'is_admin',
                  )
        read_only_fields = ('date_joined',
                            'date_updated',)

