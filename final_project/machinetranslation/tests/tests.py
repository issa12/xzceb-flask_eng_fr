import unittest
import translator

class TestTranslator(unittest.TestCase): 
    def test_fr2en(self):
        print("test_fr2en")
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(translator.frenchToEnglish("bonjour"), "test")

    def test_en2fr(self):
        print("test_en2fr")
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(translator.englishToFrench("bonjour"), "end")

unittest.main()