from django.core.management.base import BaseCommand, CommandError
from words.models import Word, WordDescription, WordGroup  # Replace with your actual model names and app name
import json

class Command(BaseCommand):
    help = 'Import words from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to import')

    def handle(self, *args, **options):
        with open(options['json_file'], 'r', encoding='utf-8') as file:
            data = json.load(file)

        for language, content in data.items():
            description_translations = content['description']
            # Assuming you have a WordGroup model for each language
            word_group, created = WordGroup.objects.get_or_create(name=language)

            # Update descriptions for each language
            for lang_code, description in description_translations.items():
                setattr(word_group, f'description_{lang_code}', description)
            word_group.save()

            # Now add words
            for word_item in content['words']:
                word, created = Word.objects.get_or_create(
                    word=word_item['word'],
                    word_group=word_group,
                    defaults={'quiz_type': word_item['quiz_type']}
                )

                # Add descriptions for the word in different languages
                for lang_code, description in word_item['descriptions'].items():
                    WordDescription.objects.get_or_create(
                        word=word,
                        language=lang_code,
                        defaults={'description': description}
                    )
        
        self.stdout.write(self.style.SUCCESS('Successfully imported words'))
