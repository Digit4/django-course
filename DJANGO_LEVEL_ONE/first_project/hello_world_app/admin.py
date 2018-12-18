from django.contrib import admin
from hello_world_app.models import Topic,AccessRecord,WebPage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)