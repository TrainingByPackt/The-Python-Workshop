import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise10
        self.exercises = Exercise10

    def test(self):
        self.assertEqual(self.exercises.customer.full_name, 'Mary Lou')

        
if __name__ == '__main__':
    unittest.main()
   