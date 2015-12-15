import re
from patterns.pattern_core import PatternCore


class PatternClass(PatternCore):
    name = 'class'
    regex_string = '^class (.*):$'

    def __init__(self):
        self.regex = re.compile(self.regex_string)

    def extract(self, data):
        return self.search(data).group(1)

    def extract_all(self, data):
        return self.search(data).group(0)
