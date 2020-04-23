import unittest

from api_fun import apiLogic

class test_api(unittest.TestCase):

  def test_spec1(self):
    va = [{'name': 'egypt', 'area':1002450.0 , 'population': 91290000}]
    spec = apiLogic()
    out = spec.spec1(va,"area")
    self.assertEqual(out,"area=1002450.0")

  def test_spec2(self):
    va = [{'name': 'egypt', 'area':1002450.0 , 'population': 91290000}]
    spec = apiLogic()
    out = spec.spec2(va,"area","population")
    self.assertEqual(out,"area=1002450.0 , population=91290000")