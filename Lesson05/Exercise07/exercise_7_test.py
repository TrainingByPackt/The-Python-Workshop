import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise07
        self.exercises = Exercise07
        
    def test_chat(self):
        self.assertEqual(self.exercises.chad.population, 100)
        
        
if __name__ == '__main__':
    unittest.main()
   

