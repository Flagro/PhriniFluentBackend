from django.contrib import admin
from .models import Language, WordGroup, WordGroupDescription, Word, WordDescription


# Inline classes for nested relationships
class WordGroupDescriptionInline(admin.TabularInline):
    model = WordGroupDescription
    extra = 1


class WordDescriptionInline(admin.TabularInline):
    model = WordDescription
    extra = 1


class WordInline(admin.TabularInline):
    model = Word
    extra = 1


# Admin classes
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "language_name",
    )
    search_fields = ("language_name",)


@admin.register(WordGroup)
class WordGroupAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_global",
        "owner",
    )
    list_filter = (
        "is_global",
        "languages",
    )
    inlines = [WordGroupDescriptionInline, WordInline]
    search_fields = ("name",)
    raw_id_fields = ("owner",)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "word_group",
    )
    inlines = [WordDescriptionInline]
    search_fields = ("text",)
    list_filter = ("word_group",)
    raw_id_fields = ("word_group",)


# Since WordGroupDescription and WordDescription are used as inlines, they don't need to be registered directly
# But if you want to manage them separately as well, you can register them like this:


@admin.register(WordGroupDescription)
class WordGroupDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "word_group",
        "language",
        "description_text",
    )
    list_filter = (
        "word_group",
        "language",
    )
    search_fields = ("description_text",)


@admin.register(WordDescription)
class WordDescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "word",
        "language",
        "description_text",
    )
    list_filter = (
        "word",
        "language",
    )
    search_fields = ("description_text",)


# Optional: If you want to customize the admin site header and title
admin.site.site_header = "PhriniFluent Backend Admin"
admin.site.site_title = "PhriniFluent Backend Admin Portal"
admin.site.index_title = "Welcome to the PhriniFluent Backend Portal"
