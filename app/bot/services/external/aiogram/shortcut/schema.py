"""
schema shortcuts
"""


def get_schema(items):
    """
    get the schema of the items
    """
    if items == 1:
        return [1]

    if items // 2 == 0:
        return [2, 2]

    if items // 2 == 1:
        return [2, 1]
