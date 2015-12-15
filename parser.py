from repository import pattern_repository
from exceptions import NotFoundException


class Extracter:
    def __init__(self, f):
        f.seek(0)
        self.f = f
        self.lines = f.readlines()

    def evaluate_by_line(self, call_back):
        matches = []
        for line in self.lines:
            try:
                matches.append(call_back(line))
            except NotFoundException:
                continue
        return matches

    def extract(self, pattern_name):
        extract = pattern_repository.extract(pattern_name)
        return self.evaluate_by_line(call_back=extract)

    def extract_all(self, pattern_name):
        extract_all = pattern_repository.extract_all(pattern_name)
        return self.evaluate_by_line(call_back=extract_all)
