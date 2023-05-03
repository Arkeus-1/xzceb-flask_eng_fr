import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        value='Hello'
        message='The input is null.'
        self.assertIsNotNone(english_to_french(value),message)
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_frenchtoEnglish(self):
        value='Bonjour'
        message='The input is  null.'
        self.assertIsNotNone(french_to_english(value),message)
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__== '__main__':
    unittest.main()