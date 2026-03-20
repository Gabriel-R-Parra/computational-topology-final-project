import json

def get_json(field=None):
    """
        Loads json from a metadata.json file. 

        This is honestly pretty terrible in practice, but I wanted to use json to quickly update things outside of the code so it is what it is.
    """
    with open("metadata.json", "r") as _md:
        md = json.load(_md)
    if field:
        return md[field]
    else:
        return md