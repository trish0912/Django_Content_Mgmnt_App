from django.contrib import admin
from .models import Topic, Entries, Comment

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entries)
admin.site.register(Comment)

