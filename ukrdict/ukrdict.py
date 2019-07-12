# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class WordNotFound(Exception):
    """Exception for the case when the word is not found"""


def find_word(word: str) -> str:
    """
    Makes request to search for the word meaning in ukrainian dict.

    :param word: word to search for.
    :return: word meaning or raises exception if the word not found.
    """

    DICT_URL = "http://sum.in.ua/?swrd="
    req = requests.get(f"{DICT_URL}{word}")
    soup = BeautifulSoup(req.text, "lxml")

    article_body = soup.find(itemprop="articleBody")

    if not article_body:
        raise WordNotFound(f"Sorry, requested word not found.")

    content = article_body.contents

    extracted_text = ""
    for tag in content:
        extracted_text += tag.text + "\n" if tag.find(itemprop="headline") else tag.text

    return extracted_text
