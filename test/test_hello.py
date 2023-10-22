import unittest

from hello import hello

class TestHello(unittest.TestCase):
    def test_helen(self):
        # Define a name
        name = 'Helen'
        # Call the function
        message = hello.hello(name)

        # Assert that the function returns the correct string
        self.assertEqual(message, 'Hello, Helen!')

    # Add a test checking that the function fails when an integer is passed
    def test_integer(self):
        # Define a name
        name = 123
        # Call the function
        with self.assertRaises(TypeError):
            message = hello.hello(name)

if __name__ == '__main__':
    unittest.main()     
