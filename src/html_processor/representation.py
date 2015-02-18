__author__ = 'gyorgyorosz'

from collections import namedtuple

import justext


PageElement = namedtuple("PageElement", ["path", "is_content"])


def flat_list_representation(html_content, language="Hungarian"):
    pars = justext.justext(html_content, justext.get_stoplist(language))
    return [PageElement(path=par.xpath, is_content=not par.is_boilerplate) for par in pars]


def demo():
    import sys

    content = open(sys.argv[1]).read()
    for e in flat_list_representation(content):
        print(e)


if __name__ == "__main__":
    demo()
