class NotFoundException(Exception):
    def __init__(self, name, regex_string):
        self.name = name
        self.regex_string = regex_string

    def __str__(self):
        return (
            'No matches found about the following pattern.\n' +
            'PATTERN_NAME:  ' + repr(self.name) + '\n' +
            'REGEX: ' + repr(self.regex_string)
        )


class NotRegisteredPatternException(Exception):
    def __init__(self, pattern_name):
        self.pattern_name = patter_name

    def __str__(self):
        return (
            "Not registered the following pattern. Perhaps, don't you miss-spell?\n" +
            'PATTERN_NAME:  ' + repr(self.pattern_name)
        )
