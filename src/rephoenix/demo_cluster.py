import numpy

from rephoenix.distance import similarity


__author__ = 'gyorgyorosz'

import os
from sklearn.cluster import SpectralClustering
from rephoenix.representation import flat_list_representation


def get_files(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        matches.extend([os.path.join(root, f) for f in filenames if f[-4:] == "html"])
    return matches


def get_representation(file_path):
    with open(file_path) as f:
        return flat_list_representation(f.read())


def demo():
    import sys

    print("Reading files")
    files = get_files(sys.argv[1])
    pages = [get_representation(f) for f in files]
    clustering = SpectralClustering(affinity="precomputed")
    print("Computing similarity matrix")
    sim_matrix = numpy.array([[similarity(page_i, page_j) for page_j in pages] for page_i in pages])
    print("Clustering")
    clustering.fit(
        sim_matrix
    )


if __name__ == "__main__":
    demo()
