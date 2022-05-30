from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50)
    github_id = models.IntegerField()
    avatar = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'{ self.username }'


class Message(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    text = models.CharField(max_length=140)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_('User'))

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return f'{ self.text[:20] }'