from string_find_cls import Find


def test_case_cls_new1():
    """
    Test find class case 1 - (Single result)
    """
    data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
    query = "eos"
    result = Find(data, query)
    assert result == ["seo"]
    assert len(result) == 1


def test_case_cls_new2():
    """
    Test find class case 2 - (Multiple results)
    """
    data = [
        "baseball",
        "juice",
        "glove",
        "cold",
        "thrill",
        "boil",
        "lovely",
        "bear",
        "dust",
        "cheat",
        "eight",
        "day",
        "relax",
        "bustling",
        "pencil",
        "calendar",
        "superficial",
        "skillful",
        "fowl",
        "condemned",
        "invent",
        "provide",
        "tiger",
        "unsightly",
        "fretful",
        "door",
        "needy",
        "uttermost",
        "slave",
        "agonizing",
        "humor",
        "space",
        "physical",
        "fasten",
        "action",
        "wren",
        "hope",
        "wipe",
        "childlike",
        "obtainable",
        "icky",
        "arrogant",
        "holiday",
        "cat",
        "lettuce",
        "whistle",
        "deceive",
        "fade",
        "sun",
        "rifle",
        "table",
        "grin",
        "mysterious",
        "luxuriant",
        "crate",
        "health",
        "easy",
        "legs",
        "tender",
        "thrill",
        "knotty",
        "malicious",
        "prose",
        "haircut",
        "juice",
        "army",
        "sleep",
        "dangerous",
        "exciting",
        "steel",
        "loose",
        "chief",
        "week",
        "obeisant",
        "delay",
        "hover",
        "act",
        "icy",
        "regular",
        "level",
        "yell",
        "unequaled",
        "obtain",
        "join",
        "cherry",
        "stocking",
        "encouraging",
        "boorish",
        "caption",
        "kneel",
        "close",
        "hospitable",
        "barbarous",
        "box",
        "vacation",
        "rot",
        "caption",
        "wilderness",
        "unruly",
        "advise",
    ]
    query = "cat"
    result = Find(data, query)
    assert result == ["cat", "act"]
    assert len(result) == 2


def test_case_cls_new3():
    """
    Test find class case 3 - (Data not found!)
    """
    data = []
    query = "cat"
    result = Find(data, query)
    assert result == "data not found!"


def test_case_cls_new4():
    """
    Test find class case 4 - (Query not found!)
    """
    data = ["sample"]
    query = ""
    result = Find(data, query)
    assert result == "query not found!"


def test_case_cls_new5():
    """
    Test find class case 5 - (Data and query not found)
    """
    data = []
    query = None
    result = Find(data, query)
    assert result == "data and query not found!"


def test_case_cls_new6():
    """
    Test find class case 6 - (Data should be a list type)
    """
    data = None
    query = None
    result = Find(data, query)
    assert result == "data should be a list type"


def test_case_cls_new7():
    """
    Test find class case 7 - (No result)
    """
    data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
    query = "test"
    result = Find(data, query)
    assert result == []
    assert len(result) == 0
