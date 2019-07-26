# -*- coding: utf-8 -*-
import pkg_resources

from ukrdict import __version__


def test_version():
    assert __version__ == pkg_resources.get_distribution("ukrdict").version
