from string_find import find

def test_case1():
    """
        Test string_find function case 1 - (Single result)
    """
    data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
    query = "eos"
    result = find(data, query)
    assert result == ["seo"]
    assert len(result) == 1

def test_case2():
    """
        Test string_find function case 2 - (Multiple results)
    """
    data = [
        "baseball", "juice", "glove", "cold", "thrill", "boil", "lovely", "bear", "dust", "cheat", "eight", 
        "day", "relax", "bustling", "pencil", "calendar", "superficial", "skillful", "fowl", "condemned", 
        "invent", "provide", "tiger", "unsightly", "fretful", "door", "needy", "uttermost", "slave", "agonizing", 
        "humor", "space", "physical", "fasten", "action", "wren", "hope", "wipe", "childlike", "obtainable", 
        "icky", "arrogant", "holiday", "cat", "lettuce", "whistle", "deceive", "fade", "sun", "rifle", 
        "table", "grin", "mysterious", "luxuriant", "crate", "health", "easy", "legs", "tender", "thrill", "knotty", 
        "malicious", "prose", "haircut", "juice", "army", "sleep", "dangerous", "exciting", "steel", "loose", 
        "chief", "week", "obeisant", "delay", "hover", "act", "icy", "regular", "level", "yell", "unequaled", 
        "obtain", "join", "cherry", "stocking", "encouraging", "boorish", "caption", "kneel", "close", "hospitable", 
        "barbarous", "box", "vacation", "rot", "caption", "wilderness", "unruly", "advise"
        ]
    query = "cat"
    result = find(data, query)
    assert result == ["cat", "act"]
    assert len(result) == 2

def test_case3():
    """
        Test string_find function case 3 - (Data not found!)
    """
    data = []
    query = "cat"
    result = find(data, query)
    assert result == "data not found!"

def test_case4():
    """
        Test string_find function case 4 - (Query not found!)
    """
    data = ["sample"]
    query = ""
    result = find(data, query)
    assert result == "query not found!"

def test_case5():
    """
        Test string_find function case 5 - (Data and query not found)
    """
    data = []
    query = None
    result = find(data, query)
    assert result == "data and query not found!"

def test_case6():
    """
        Test string_find function case 6 - (Data should be a list type)
    """
    data = None
    query = None
    result = find(data, query)
    assert result == "data should be a list type"

def test_case7():
    """
        Test string_find function case 7 - (No result)
    """
    data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
    query = "test"
    result = find(data, query)
    assert result == []
    assert len(result) == 0