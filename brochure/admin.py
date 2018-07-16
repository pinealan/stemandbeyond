from django.contrib import admin

from .models import Speaker, Metatag, Content, Affiliate

# Register your models here.
admin.site.register(Speaker)
admin.site.register(Metatag)
admin.site.register(Content)
admin.site.register(Affiliate)
