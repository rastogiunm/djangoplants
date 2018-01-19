from django.db import models

class Plant(models.Model):
    #PlantId is Id
    SpeciesId = models.IntegerField()
    Name = models.CharField(max_length = 500)
    Family = models.TextField(blank=True)
    ScientificName = models.TextField(blank=True)
    Synonyms = models.TextField(blank=True)
    VernacularName = models.TextField(blank=True)
    REDCode = models.TextField(blank=True)
    Description = models.TextField(blank=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class PlantPhoto(models.Model):
    """
    Model representing plant photos.
    """
    
    plant = models.ForeignKey('Plant', on_delete=models.SET_NULL, null=True) 
    photo_name = models.CharField(max_length=200)

    def __str__(self):
        return self.photo_name
