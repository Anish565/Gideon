# pip install googletrans==4.0.0-rc1
from googletrans import Translator,constants
from pprint import pprint

import googletrans

from speakLanguageAudio import langOutput

def trans(t,frm, to):
    translator = Translator(service_urls=[
        'translate.google.com'
    ])
    # print(googletrans.LANGUAGES)

    try:
        # print(t)
        translatedText = translator.translate(t,dest=to,src="auto")
        # print(translatedText)
        translatedText = translatedText.text
        # print(translatedText)
        langOutput(translatedText,'es')
        return translatedText
    except Exception as e:
        print(e)


# print(trans("Hi I am going to a party in the middle of the city",'en','es'))
