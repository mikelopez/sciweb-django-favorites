from django.db import models

# Create your models here.
class Topic(models.Model):
    """
    very basic topic table
    """
    name = models.CharField(max_length=20)
    image_url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    


