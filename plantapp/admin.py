from django.contrib import admin
from plantapp.models import Plant, PlantPhoto

#admin.site.register(Plant)

class PlantPhotoInline(admin.TabularInline):
    """
    Defines format of inline book instance insertion (used in BookAdmin)
    """
    model = PlantPhoto

class PlantAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    #list_display = ('title', 'author', 'display_genre')
    inlines = [PlantPhotoInline]

admin.site.register(Plant, PlantAdmin)