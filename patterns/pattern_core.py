from exceptions import NotFoundException


class PatternCore:
    name = None
    regex_string = None

    def __init__(self):
        """create self.regex from regex_string"""
        raise NotImplementedError()

    def search(self, data):
        founds = self.regex.search(data)
        if not founds:
            raise NotFoundException(self.name, self.regex_string)
        return founds

    def extract(self, data):
        """return groups match about self.regex_string(e.g. return m.group(1))"""
        raise NotImplementedError()

    def extract_all(self, data):
        """return data if match about self.regex_string(e.g. return m.group(0))"""
        raise NotImplementedError()
