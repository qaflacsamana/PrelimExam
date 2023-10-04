import unittest

def name():
    x = 'juan'
    return x.upper()

class Checker (unittest.TestCase):
    def test_name(self):
        self.assertEqual(name(), "MIGUEL")

if __name__ == '__main__':
    unittest.main()
