import sys
import unittest
from unittest import TestCase, TestSuite, TextTestRunner
from decimal import Decimal

sys.path.append('favorites')
#sys.path.append('favorites/tests')

from tests import FavoritesTest

if __name__ == '__main__':
    unittest.main()
