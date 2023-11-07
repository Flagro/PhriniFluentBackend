from django.contrib import admin
from .models import (
    Language, WordGroup, Word, WordDescription, UserWordGroup
)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_tag', 'language_name')
    search_fields = ('language_tag', 'language_name')

@admin.register(WordGroup)
class WordGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'is_global')
    list_filter = ('language', 'is_global')
    search_fields = ('name', 'description')

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('text', 'language', 'word_group')
    list_filter = ('language', 'word_group')
    search_fields = ('text',)

@admin.register(WordDescription)
class WordDescriptionAdmin(admin.ModelAdmin):
    list_display = ('word', 'language', 'description_text')
    list_filter = ('language',)
    search_fields = ('word__text', 'description_text')

@admin.register(UserWordGroup)
class UserWordGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'word_group', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('user__username', 'word_group__name')

# Optional: If you want to customize the admin site header and title
admin.site.site_header = "PhriniFluent Backend Admin"
admin.site.site_title = "PhriniFluent Backend Admin Portal"
admin.site.index_title = "Welcome to the PhriniFluent Backend Portal"
