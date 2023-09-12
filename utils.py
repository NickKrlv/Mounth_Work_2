import requests
import json
from random import choice
from classes import BasicWord
import urllib3


urllib3.disable_warnings()


def load_random_word(path):
    '''Загружает случайное слово из json-файла с интернет ресурса'''
    data = requests.get(url=path, verify=False)
    data_json = json.loads(data.text)
    word = choice(data_json)
    return BasicWord(word['word'], word['subwords'])
