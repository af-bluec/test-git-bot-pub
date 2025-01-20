import unittest
from src.greeting import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

if __name__ == "__main__":
    unittest.main()
