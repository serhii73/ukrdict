# -*- coding: utf-8 -*-

import click

from .ukrdict import find_word


@click.command()
@click.argument("word", nargs=1)
def main(word):
    """
    CLI call example:
    >>> ukrdict жовтогарячий

    Searches for the specified word and returns its meaning to CLI stdout.
    :param word: word to search for
    :return:  word meaning or raises exception if the word not found.
    """
    res = find_word(word)
    click.echo(res)
    return None


if __name__ == "__main__":
    main()
