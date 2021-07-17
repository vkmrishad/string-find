from string_find import find


class Find:
    """
    Class that will find all exact words from list of words.
    """

    def __new__(cls, data, query):
        return find(data, query)
