import json
import os
def getServers():
    serverjsonfile = os.getenv("MONITER_SERVERJSONFILE")
    if serverjsonfile is None: raise Exception('MONITER_SERVERJSONFILE env not found or empty')
    with open(serverjsonfile) as jsonfile:
        file = json.load(jsonfile)
    return file

