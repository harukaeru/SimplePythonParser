from patterns.pattern_class import PatternClass
from exceptions import NotRegisteredPatternException


class PatternRepository(dict):
    def add(self, pattern):
        self[pattern.name] = pattern
        return self

    def find(self, pattern_name):
        pattern = self.get(pattern_name)
        if not pattern:
            raise NotRegisteredPatternException(pattern_name)
        return pattern

    def extract(self, pattern_name):
        pattern = self.find(pattern_name)
        return pattern.extract

    def extract_all(self, pattern_name):
        pattern = self.find(pattern_name)
        return pattern.extract_all


pattern_repository = PatternRepository()
pattern_repository.add(PatternClass())
