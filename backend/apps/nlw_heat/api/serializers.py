from rest_framework import serializers
from ..models import Message, Profile


class MessageSerializer(serializers.ModelSerializer):
    '''Message Serializer'''
    user_name = serializers.SerializerMethodField()
    user_avatar = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.name or obj.user.username

    def get_user_avatar(self, obj):
        return obj.user.avatar

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['user']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
