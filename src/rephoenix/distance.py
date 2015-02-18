__author__ = 'korommatyi'

import difflib


def similarity(o1, o2):
    sm = difflib.SequenceMatcher(a=o1, b=o2)
    return sm.ratio()
    # d = 0
    # for t in sm.get_opcodes():
    #     operation = t[0]
    #     if operation == 'insert':
    #         d += t[4] - t[3]
    #     elif operation == 'delete':
    #         d += t[2] - t[1]
    #     elif operation == 'replace':
    #         d += max(t[4] - t[3], t[2] - t[1])


def median(cluster):
    if len(cluster) == 1:
        return cluster[0]
    s1 = cluster[0]
    s2 = cluster[1]
    c = []
    blocks = difflib.SequenceMatcher(a=s2, b=s1).get_matching_blocks()
    for b in blocks:
        c.extend(s1[b[0]:(b[0] + b[2] + 1)])
    return c
