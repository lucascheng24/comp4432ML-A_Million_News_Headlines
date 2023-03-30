import os
from smart_open import smart_open
from gensim.models.word2vec import Text8Corpus
from gensim.downloader import base_dir


class Dataset(object):
    def __init__(self, fn):
        self.fn = fn

    def __iter__(self):
        corpus = Text8Corpus(self.fn)
        for doc in corpus:
            yield doc


def load_data():
    path = os.path.join(base_dir, 'text8', 'text8.gz')
    return Dataset(path)
