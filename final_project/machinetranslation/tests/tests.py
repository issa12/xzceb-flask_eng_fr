import unittest
from machinetranslation import translator

class TestTranslator(unittest.TestCase): 
    def test_fr2en(self):
        print("test_fr2en")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("bonjour"), "test")

    def test_en2fr(self):
        print("test_en2fr")
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("bonjour"), "end")

unittest.main()