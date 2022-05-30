from django.contrib import admin
from django.conf.locale.pt_BR import formats as portuguese
from django.conf.locale.en import formats as english
from rangefilter.filters import DateRangeFilter
from .models import Message, Profile

portuguese.DATE_FORMAT = 'd/m/Y'
english.DATE_FORMAT = 'd/m/Y'


@admin.register(Message)
class MessageRegister(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['id', '__str__', 'user', 'created_at']
    list_display_links = ['id', '__str__']
    list_filter = [
        'user',
        ('created_at', DateRangeFilter),
    ]
    list_per_page = 25
    ordering = ['id']
    search_fields = ['id', 'text', 'user']

    # def likes_count(self, obj):
    #     return obj.likes.all().count()
    # likes_count.short_description = 'Likes'


@admin.register(Profile)
class ProfileRegister(admin.ModelAdmin):
    # autocomplete_fields = ['user']
    list_display = ['id', '__str__', 'name', 'created_at']
    list_display_links = ['id', '__str__']
    list_filter = [
        ('created_at', DateRangeFilter),
    ]
    list_per_page = 25
    ordering = ['id']
    search_fields = ['id', '__str__']
