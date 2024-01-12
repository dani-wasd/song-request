from django.contrib import admin
from .models import streamer, SongRequest

# Register your models here.
admin.site.register(streamer)
admin.site.register(SongRequest)
