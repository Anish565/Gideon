from googletrans import Translator,constants
from pprint import pprint

def trans(t):
    translator=Translator()
    translation = translator.translate(t)
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print(translation.text)
    return translation.text
