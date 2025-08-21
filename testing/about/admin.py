from django.contrib import admin
from .models import AboutUs

# Register your models here
# 
# .
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['title','about_data']



admin.site.register(AboutUs,AboutUsAdmin)