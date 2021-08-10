# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv



load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishtofrench(text1):
    """
    This function translates english to french
    """
    authenticator = IAMAuthenticator('Ep9u8f5eDvX_kWn2pXP4vuwXfK86bKgf6BBlG6SDFPxR')
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
    language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/612bbd37-84b6-4b25-8220-fcfb704b2393')

    frenchtranslation=language_translator.translate(
    text=text1, model_id='en-fr').get_result()

    return frenchtranslation.get("translations")[0].get("translation")

def frenchtoenglish(text1):
    """
    This function translates french to english
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
    language_translator.set_service_url(url)

    englishtranslation=language_translator.translate(
    text=text1, model_id='fr-en').get_result()

    return englishtranslation.get("translations")[0].get("translation")
    
