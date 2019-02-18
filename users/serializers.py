from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # photo = serializers.FilePathField(path='tmp')
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'pseudonym')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('date_joined',
                            'date_updated',)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            pseudonym=validated_data['pseudonym']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
