from models import Favorites, FavoriteItem
from django.contrib.auth.models import User
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):

    def setUp(self):
        try:
            self.user = User.objects.get(username='usertest1')
        except User.DoesNotExist:
            self.user = User.objects.create(username='usernametest1')

    def test_add_get_favorite(self):
        """
        test adding a favorite for the user on FavoriteItem
        no duplicates for favorites!
        """
        favitem = FavoriteItem(name='Product 1')
        favitem.save()
        fav = Favorites.objects.add_favorite(self.user, favitem)
        self.assertTrue(len(Favorites.objects.all()) == 1)

        # should not duplicate
        if not Favorites.objects.get_favorite(favitem, self.user):
            fav_duplicate = Favorites.objects.add_favorite(self.user, favitem)

        fav_len = len(Favorites.objects.all())
        print "%s rows found " % fav_len
        self.assertTrue(fav_len == 1)

        favget = Favorites.objects.get_favorite(favitem, self.user)
        self.assertTrue(favget)

        


