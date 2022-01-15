from django.contrib import admin
from .models import Authors,Releases,Articles,Genres
# Register your models here.

admin.site.register(Articles)
admin.site.register(Authors)
admin.site.register(Releases)
admin.site.register(Genres)
