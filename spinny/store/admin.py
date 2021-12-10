from django.contrib import admin
from .models import Box

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display=['id','user','length','width','height','area','volume','last_modified_by','created_on']