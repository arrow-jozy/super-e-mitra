from django.contrib import admin
from formfill.models import Formfill,UserformImage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('form_details',)

admin.site.register(Formfill)
admin.site.register(UserformImage)