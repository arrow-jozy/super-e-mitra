from django.contrib import admin
from formfill.models import Form,Userform,UserformImage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('form_details',)

admin.site.register(Form, PostAdmin)
admin.site.register(Userform)
admin.site.register(UserformImage)