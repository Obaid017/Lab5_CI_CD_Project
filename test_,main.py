import unittest 
from main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4,3),7)

if __name__ == "__main__":
    unittest.main()