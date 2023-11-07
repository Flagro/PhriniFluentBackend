from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined
    telegram_handle = models.CharField(max_length=100, unique=True, null=True, blank=True)


class Language(models.Model):
    language_tag = models.CharField(max_length=10)
    language_name = models.CharField(max_length=50)


class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_global = models.BooleanField(default=False)
    users = models.ManyToManyField(CustomUser, through='UserWordGroup', related_name='word_groups')


class UserWordGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Word(models.Model):
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE, related_name='words')
    text = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class WordDescription(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description_text = models.TextField()
