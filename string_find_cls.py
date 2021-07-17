from string_find import find


class Find:
    """
    Class that will find all exact words from list of words.
    """

    def __new__(cls, data, query):
        return find(data, query)


class StringFind:
    """
    Class that will find all exact words from list of words. (Approach explained in problem)
    """

    def __init__(self, data, query):
        self.data = data
        self.query = query

    def find(self):
        return find(self.data, self.query)
