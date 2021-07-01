from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # birth = serializers.CharField(source='')
    # guide = serializers.CharField(source='')
    class Meta:
        model = User
        # fields = ['id', 'account_name', 'users', 'created']
        exclude = ['title', 'language', 'linenos', 'style']


'''
class UserSerializer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
'''
