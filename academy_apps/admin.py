from django.contrib import admin
from .models import *

class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# admin.site.register(Post_rus, SlugAdmin)
# admin.site.register(Post, SlugAdmin)
admin.site.register(Carausel)