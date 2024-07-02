import unittest
import os
import tempfile
from unittest.mock import patch
from io import StringIO
import main  # Import the main script

class TestBingoGenerator(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with sample bingo items
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.temp_file.write('\n'.join([f'Item {i}' for i in range(1, 26)]))
        self.temp_file.close()

    def tearDown(self):
        # Remove the temporary file
        os.unlink(self.temp_file.name)

    def test_read_items(self):
        items = main.read_items(self.temp_file.name)
        self.assertEqual(len(items), 25)
        self.assertEqual(items[0], 'Item 1')
        self.assertEqual(items[-1], 'Item 25')

    def test_generate_bingo_card_with_free(self):
        items = main.read_items(self.temp_file.name)
        card = main.generate_bingo_card(items, use_free_square=True)
        self.assertEqual(len(card), 25)
        self.assertEqual(card[12], 'FREE')
        self.assertNotEqual(set(card), set(items))  # Check that items are shuffled

    def test_generate_bingo_card_without_free(self):
        items = main.read_items(self.temp_file.name)
        card = main.generate_bingo_card(items, use_free_square=False)
        self.assertEqual(len(card), 25)
        self.assertNotIn('FREE', card)
        self.assertNotEqual(set(card), set(items))  # Check that items are shuffled

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_free(self, mock_stdout):
        test_output = 'test_output.pdf'
        with patch('sys.argv', ['main.py', self.temp_file.name, '1', test_output]):
            main.main()
        self.assertTrue(os.path.exists(test_output))
        os.remove(test_output)
        self.assertIn("1 bingo cards have been generated", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_without_free(self, mock_stdout):
        test_output = 'test_output.pdf'
        with patch('sys.argv', ['main.py', self.temp_file.name, '1', test_output, '--no-free']):
            main.main()
        self.assertTrue(os.path.exists(test_output))
        os.remove(test_output)
        self.assertIn("1 bingo cards have been generated", mock_stdout.getvalue())

    def test_main_not_enough_items(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write('\n'.join([f'Item {i}' for i in range(1, 24)]))  # Only 23 items
        
        with patch('sys.argv', ['main.py', temp_file.name, '1', 'test_output.pdf']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main.main()
        
        self.assertIn("Error: Input file must contain at least 24 items.", mock_stdout.getvalue())
        os.unlink(temp_file.name)

if __name__ == '__main__':
    unittest.main()
