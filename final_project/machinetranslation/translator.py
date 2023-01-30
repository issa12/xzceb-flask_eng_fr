"""
Test IBM translate service
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(english_text):
    """
    Translate from English to french
    """
    french_text = language_translator.translate(text=english_text,  model_id='en-fr').get_result()
    return french_text

def frenchToEnglish(french_text):
    """
    Translate from French to English
    """
    english_text = language_translator.translate( text=french_text,  model_id='fr-en').get_result()
    return english_text
