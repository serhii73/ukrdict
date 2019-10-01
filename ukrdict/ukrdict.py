from typing import Optional

import requests
from bs4 import BeautifulSoup


def get_page_content(w: str) -> BeautifulSoup:
    DICT_URL = "http://sum.in.ua/?swrd="
    req = requests.get(f"{DICT_URL}{w}")
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def get_word(bs: BeautifulSoup) -> Optional[str]:
    article_body = bs.find(itemprop="articleBody")
    if not article_body:
        return None

    content = article_body.contents
    lines = [tag.text for tag in content]
    extracted_text = "".join(lines)
    return extracted_text or None


def get_alternatives(bs: BeautifulSoup) -> Optional[str]:
    alternatives = bs.find(id="search-res")
    if not alternatives:
        return None

    header = alternatives.p.text
    extracted_text = header
    if alternatives.ul:
        words = [w.text for w in alternatives.ul]
        extracted_text += extracted_text + "\n" + "\n".join(words)
    return extracted_text


def find_word(word: str) -> str:
    cont = get_page_content(word)
    return (
        get_word(cont)
        or get_alternatives(cont)
        or f"Слова «{word}» не знайдено"
    )
