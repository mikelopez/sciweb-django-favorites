"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from models import Favorites, FavoriteItem
from django.contrib.auth.models import User
try:
    from termprint import *
except ImportError:
    def termprint(log, data):
        print "%s:: %s" % (log, data)

from django.test import TestCase
from django.core.urlresolvers import reverse
from templatetags.favorite_tags import my_favorites

class FavoritesTest(TestCase):

    def setUp(self):
        self.user = User.objects.get_or_create(username='usertest1')
        self.user.set_password('test123')
        self.user.save()
        
       
    def test_ajax_favorite_status(self):
        """Tests ajax url to check on item favorited stats"""
        # first create a sample item to be favorited
        favitem = FavoriteItem(name='Product 1')
        favitem.save()
        client = Client()
        client.login(username=self.user.username, 'test123')
        response = client.get(reverse('in_favorites', kwargs={'content_type': ctype,
                                                              'object_id': objectid}))

    def test_add_get_favorite(self):
        """
        test adding a favorite for the user on FavoriteItem
        no duplicates for favorites!
        """
        favitem = FavoriteItem(name='Product 1')
        favitem.save()
        self.assertFalse(Favorites.objects.get_favorite(self.user, favitem))

        fav = Favorites.objects.add_favorite(self.user, favitem)
        fav_len = len(Favorites.objects.all())
        self.assertTrue(fav_len == 1)

        # should not duplicate
        if not Favorites.objects.get_favorite(self.user, favitem):
            termprint("WARNING", 'Not found....adding')
            fav_duplicate = Favorites.objects.add_favorite(self.user, favitem)

        fav_len = len(Favorites.objects.all())
        termprint("INFO", "%s rows found " % fav_len)
        self.assertTrue(fav_len == 1)

        favget = Favorites.objects.get_favorite(self.user, favitem)
        self.assertTrue(favget)

        # test the templat tag get
        termprint("INFO", my_favorites(self.user))
        self.assertTrue(my_favorites(self.user))


    def test_remove_get_favorite(self):
        """
        test adding a favorite for the user on FavoriteItem
        no duplicates for favorites!
        """
        favitem = FavoriteItem(name='Product 1')
        favitem.save()
        self.assertFalse(Favorites.objects.get_favorite(self.user, favitem))

        fav = Favorites.objects.add_favorite(self.user, favitem)
        fav_len = len(Favorites.objects.all())
        self.assertTrue(fav_len == 1)

        # delete it
        fav_del = Favorites.objects.delete_favorite(self.user, favitem)

        fav_len = len(Favorites.objects.all())
        self.assertTrue(fav_len == 0)

        termprint("INFO", my_favorites(self.user))
        self.assertFalse(my_favorites(self.user))



