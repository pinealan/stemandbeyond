from django.contrib import admin

from .models import Speaker, Metatag, Content

# Register your models here.
admin.site.register(Speaker)
admin.site.register(Metatag)
admin.site.register(Content)
