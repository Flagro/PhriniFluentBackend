from django.db import models
from phrini_fluent_users.models import PhriniFluentUser


class Language(models.Model):
    language_name = models.CharField(max_length=50)


class WordGroup(models.Model):
    name = models.CharField(max_length=100)
    is_global = models.BooleanField(default=False)  # Indicates if the word group is public
    owner = models.ForeignKey(
        PhriniFluentUser,
        on_delete=models.CASCADE,
        related_name='owned_word_groups',
        null=True,  # Null signifies a public word group if no owner is set
        blank=True
    )
    languages = models.ManyToManyField(Language, through='WordGroupDescription')


class WordGroupDescription(models.Model):
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description_text = models.TextField()


class Word(models.Model):
    word_group = models.ForeignKey(WordGroup, on_delete=models.CASCADE, related_name='words')
    text = models.CharField(max_length=100)


class WordDescription(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='descriptions')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description_text = models.TextField()
