from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "email", "full_name", "password", "is_active", "date_joined"]
        read_only_fields = ["id", "is_active", "date_joined"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        return User.objects.create_user(password=password, **validated_data)
