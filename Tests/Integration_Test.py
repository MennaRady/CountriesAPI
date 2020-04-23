
import unittest
from api import getBySpec1


class test_system (unittest.TestCase):


    def test_Integration1(self):
       cu = getBySpec1("egypt", "area")
       va = "area=1002450.0"
       self.assertEqual(cu, va)


    def test_Integration2(self):
        cu = getBySpec1("egypt", "area,population")
        va = "area=1002450.0 , population=91290000"
        self.assertEqual(cu, va)








