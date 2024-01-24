from rest_framework import serializers
from .models import CustomUser, Role, Item

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'roles']

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])  
        roles = [Role.objects.get_or_create(**role_data)[0] for role_data in roles_data]
        user = CustomUser.objects.create(**validated_data)
        user.roles.set(roles)

        return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
