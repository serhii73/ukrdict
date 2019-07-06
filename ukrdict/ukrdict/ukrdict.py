# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class WordNotFound(Exception):
    pass


def find_word(word: str) -> str:
    """
    Makes request to search for the word meaning in ukrainian dict.

    :param word: word to search for.
    :return: word meaning or raises exception if the word not found.
    """

    DICT_URL = 'http://sum.in.ua/?swrd='
    req = requests.get(f'{DICT_URL}{word}')
    soup = BeautifulSoup(req.text, 'lxml')

    try:
        index_close_p = str(soup.find(itemprop='articleBody')).index('</p>')
        before_close_p = str(soup.find(itemprop='articleBody'))[:index_close_p]
        after_close_p = str(soup.find(itemprop='articleBody'))[index_close_p:]
        extract_soup = before_close_p + '\n' + after_close_p
        extract_text = BeautifulSoup(extract_soup, 'html.parser').text.strip()
    except ValueError:
        raise WordNotFound(f'Sorry, requested word not found.')
    return extract_text
