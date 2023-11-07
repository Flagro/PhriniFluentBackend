from django.core.management.base import BaseCommand
from phrini_fluent_words.models import Word, WordDescription, WordGroup, WordGroupDescription, Language
import json

class Command(BaseCommand):
    help = 'Import words from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to import')

    def handle(self, *args, **options):
        with open(options['json_file'], 'r', encoding='utf-8') as file:
            data = json.load(file)

        for language_name, content in data.items():
            word_group, created = WordGroup.objects.get_or_create(name=language_name)
            
            # Assuming you have a Language model instance for each language name
            for lang_name, description in content['description'].items():
                language, _ = Language.objects.get_or_create(language_name=lang_name)
                WordGroupDescription.objects.update_or_create(
                    word_group=word_group,
                    language=language,
                    defaults={'description_text': description}
                )

            # Now add words
            for word_item in content['words']:
                word, created = Word.objects.get_or_create(
                    text=word_item['word'],
                    word_group=word_group
                )

                # Add descriptions for the word in different languages
                for lang_name, description in word_item['descriptions'].items():
                    language, _ = Language.objects.get_or_create(language_name=lang_name)
                    WordDescription.objects.update_or_create(
                        word=word,
                        language=language,
                        defaults={'description_text': description}
                    )

        self.stdout.write(self.style.SUCCESS('Successfully imported words'))
