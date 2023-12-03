import unittest
from UPISAS.tests.your_exemplar.test_your_exemplar_interface import TestYourExemplarInterface

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestYourExemplarInterface)
    unittest.TextTestRunner().run(suite)