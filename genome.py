class GenomeData:
    def __init__(self, name, sequence, ngrams):
        self._name = name
        self._sequence = sequence
        self._ngrams = ngrams
    def get_name(self):
        return self._name
    def get_sequence(self):
        return self._sequence
    def get_ngrams(self):
        return self._ngrams