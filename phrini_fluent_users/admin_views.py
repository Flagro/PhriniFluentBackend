from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def import_words(request):
    call_command('import_words')
    return HttpResponse("Words imported successfully")
