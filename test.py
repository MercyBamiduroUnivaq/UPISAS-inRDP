import unittest
from UPISAS.tests.your_exemplar.test_suave_interface import TestSuaveInterface

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuaveInterface)
    unittest.TextTestRunner().run(suite)