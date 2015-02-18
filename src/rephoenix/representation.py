__author__ = 'gyorgyorosz'

from collections import namedtuple

import justext

from rephoenix.distance import similarity


PageElement = namedtuple("PageElement", ["path", "is_content"])


def flat_list_representation(html_content, language="Hungarian"):
    pars = justext.justext(html_content, justext.get_stoplist(language))
    return [PageElement(path=par.xpath, is_content=not par.is_boilerplate) for par in pars]


def demo():
    import sys

    content1 = open(sys.argv[1]).read()
    content2 = open(sys.argv[2]).read()
    repr1 = flat_list_representation(content1)
    repr2 = flat_list_representation(content2)
    print(similarity(repr1, repr2))



if __name__ == "__main__":
    demo()
