from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class FavoriteManager(models.Manager):
    """
    Custom manager for favorites
    """
    def get_content_type(self, obj):
        """
        return the contenttype for an object
        """
        return ContentType.objects.get_for_model(type(obj))

    def get_favorite(self, obj, user):
        """
        Get the favorite 
        """
        content_type = ContentType.objects.get_for_model(type(obj))
        return self.get_query_set().get(content_type=self.get_content_type(obj),
            object_id=obj.pk, user=user)

    def is_favorite(self, obj, user):
        """
        Check if its in your favs already
        """
        return 

    @classmethod
    def add_favorite(cls, user, content_object):
        """
        class method  applied to class as whole
        """
        content_type = ContentType.objects.get_for_model(type(content_object))
        fav = Favorites(user=user, content_type=content_type, \
            content_object=content_object, object_id=content_object.pk)
        fav.save()
        return fav


class Favorites(models.Model):
    """
    keep track of the users' favorite object
    """
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField(default=datetime.now())
    objects = FavoriteManager()


class FavoriteItem(models.Model):
    """
    favorite item object used for tests 
    """
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)





