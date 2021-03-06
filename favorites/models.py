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

    @classmethod
    def get_favorite(cls, user, obj):
        """
        get the favorite object for a user
        """
        content_type = ContentType.objects.get_for_model(type(obj))
        try:
            fav = Favorites.objects.get(user=user, content_type=content_type, \
                object_id=obj.pk)
            return fav
        except Favorites.DoesNotExist:
            return None
        except Favorites.MultipleObjectsReturned:
            # shouldnt do this but just incase
            try:
                return Favorites.objects.filter(user=user, content_type=content_type)[0]
            except IndexError:
                return None

    @classmethod
    def add_favorite(cls, user, content_object):
        """
        Add favorite item - no duplicate
        """
        if not cls.get_favorite(user, content_object):
            content_type = ContentType.objects.get_for_model(type(content_object))
            fav = Favorites(user=user, content_type=content_type, \
                content_object=content_object, object_id=content_object.pk)
            fav.save()
            return fav
        return None

    @classmethod
    def delete_favorite(cls, user, content_object):
        """
        Add favorite item - no duplicate
        If no user is passed, delete this fav instance from all users
        """
        content_type = ContentType.objects.get_for_model(type(content_object))
        filters = {'content_type': content_type, 'object_id': content_object.pk}
        if user:
            filters['user'] = user       
        for fav in Favorites.objects.filter(**filters):
            fav.delete()
        return True

    @classmethod
    def get_fav_link(self, obj):
        """
        Generate the favorite
        """
        return "/favorites/add/%s/%s" % (obj.pk, ContentType.objects.get_for_model(obj).pk)

    @classmethod
    def get_unfav_link(self, obj):
        """
        Remove the favorite
        """
        return "/favorites/remove/%s/%s" % (obj.pk, ContentType.objects.get_for_model(obj).pk)

    @classmethod
    def generate_fav_html_link(self, user, obj):
        """
        Generat ethe html favorite link based on the 
        user and object - checking if the object is favorited
        or not which will return the proper html link 
        """
        if self.get_favorite(user, obj):
            return self.get_unfav_link(obj)
        else:
            return self.get_fav_link(obj)




class Favorites(models.Model):
    """
    keep track of the users' favorite for an object
    user can like products, news, topics, all in one table
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





