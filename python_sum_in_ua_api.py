# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class NotFoundYourWord(ValueError):
    pass


class Ukrainian_Dictionary:
    def search_word(self, word):
        r = requests.get(f"http://sum.in.ua/?swrd={word}")
        soup = BeautifulSoup(r.text, "lxml")

        try:
            index_close_p = str(soup.find(itemprop="articleBody")).index("</p>")
            before_close_p = str(soup.find(itemprop="articleBody"))[:index_close_p]
            after_close_p = str(soup.find(itemprop="articleBody"))[index_close_p:]
            extract_soup = before_close_p + "\n" + after_close_p
            extract_text = BeautifulSoup(extract_soup, "html.parser").text.strip()
        except ValueError:
            raise NotFoundYourWord(f"Not found your word in this URL {r.url}")
        return extract_text

    def __repr__(self):
        return f"Ukrainian_Dictionary"
