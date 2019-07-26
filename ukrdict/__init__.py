# -*- coding: utf-8 -*-
import pkg_resources

from .ukrdict import find_word

__all__ = ["find_word"]
__version__ = pkg_resources.get_distribution("ukrdict").version
