import savepagenow
import os
import json
import uuid

def create_metadata(url):
    if not os.path.exists("schema.json"):
        print("Please create a schema.json file in the same directory as this script and fill it out with the schema generator.")
        return
    else:
        with open("schema.json", "r+", encoding="utf-8") as schema_out:
            data = json.load(schema_out)

             agency_info = data["agency_info"]