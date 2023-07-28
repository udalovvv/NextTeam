from django.contrib import admin
from gallery.models import *


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['img_name', 'img_file']
