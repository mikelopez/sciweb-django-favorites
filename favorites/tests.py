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

    def test_add_favorite(self):
        """
        test adding a favorite for the user on FavoriteItem
        """
        favitem = FavoriteItem(name='Product 1')
        favitem.save()
        fav = Favorites.objects.add_favorite(self.user, favitem)
        fav.save()
        self.assertTrue(len(Favorites.objects.all()) > 0)



