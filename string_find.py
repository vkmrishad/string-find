from typing import List


def find(data: List[str], query: str):
    """
    Function that will find all exact words from list of words.
    """
    # List for storing result.
    result = list()

    # Check if data is a list.
    if type(data) == list:
        # Check if data and query is not None.
        if data and query:
            # Loop all item in list.
            for item in data:
                # Check for length to skip sorting operation.
                if len(query) == len(query):
                    # If length matches, straight comparison. Using case insensitive comparison.
                    if str(query).lower() == str(item).lower():
                        # Push to result list
                        result.append(item)
                    # Else, sort both item and query and compare. Using case insensitive comparison.
                    else:
                        query_str = "".join(sorted(query))
                        item_str = "".join(sorted(item))
                        if str(query_str).lower() == str(item_str).lower():
                            # Push to result list
                            result.append(item)

            # Return list of result items.
            return result

        else:
            # If data and query not found
            if not data and not query:
                return "data and query not found!"
            # Elif data not found
            elif not data:
                return "data not found!"
            # Elif query not found
            elif not query:
                return "query not found!"
            else:
                return "some other error"
    else:
        return "data should be a list type"
