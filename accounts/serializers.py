from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'disp_name',
            'password',
            'is_trainer',)

    def create(self, validated_data):
        print(validated_data)
        return get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            disp_name=validated_data['disp_name'],
            password=validated_data['password'],
            is_trainer=validated_data['is_trainer'],
        )

    def update(self, instance, validated_data):
        """
        exclude email and password here because
        they are changed by a custom API.
        """
        if 'password' in validated_data:
            del validated_data['password']
        if 'email' in validated_data:
            del validated_data['email']
        return super().update(instance, validated_data)
