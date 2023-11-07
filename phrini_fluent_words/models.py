from django.db import models
from ..phrini_fluent_users.models import PhriniFluentUser


class Language(models.Model):
    language_tag = models.CharField(max_length=10)
    language_name = models.CharField(max_length=50)


class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_global = models.BooleanField(default=False)
    users = models.ManyToManyField(PhriniFluentUser, through='UserWordGroup', related_name='word_groups')


class UserWordGroup(models.Model):
    user = models.ForeignKey(PhriniFluentUser, on_delete=models.CASCADE)
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
