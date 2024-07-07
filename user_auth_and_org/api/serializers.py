from rest_framework import serializers
from users.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'password', 'phone']

    def create(self, validated_data):
        user = User(
            user_id=validated_data['user_id'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data.get('phone', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if not attrs.get('email'):
            raise serializers.ValidationError({'email': 'This field is required.'})
        if not attrs.get('first_name'):
            raise serializers.ValidationError({'first_name': 'This field is required.'})
        if not attrs.get('last_name'):
            raise serializers.ValidationError({'last_name': 'This field is required.'})
        if not attrs.get('password'):
            raise serializers.ValidationError({'password': 'This field is required.'})
        return attrs
