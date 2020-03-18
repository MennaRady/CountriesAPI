import unittest
from baseApi import baseApi
from api_fun import apiLogic
from api import getBySpec2,getBySpec1



class test_system (unittest.TestCase ):


    def test_integration1(self):
       cu = getBySpec1 ("egypt","area")
       va = "area=1002450.0"
       self.assertEqual(cu,va)


    def test_integration2 (self):
        cu = getBySpec1("egypt", "area,population")
        va = "area=1002450.0 , population=91290000"
        self.assertEqual(cu, va)








