from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telegram_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)


class APIKey(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='api_keys')
    api_key = models.CharField(max_length=40, unique=True)  # You can use a pre-save signal to generate a unique key
    date_issued = models.DateTimeField(auto_now_add=True)
    permissions = models.JSONField(default=dict)  # Store permissions as JSON
    active = models.BooleanField(default=True)


class Language(models.Model):
    language_tag = models.CharField(max_length=10)
    language_name = models.CharField(max_length=50)


class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_global = models.BooleanField(default=False)
    users = models.ManyToManyField(CustomUser, through='UserWordGroup', related_name='word_groups')


class Word(models.Model):
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE, related_name='words')
    text = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class WordDescription(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description_text = models.TextField()


class UserWordGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
