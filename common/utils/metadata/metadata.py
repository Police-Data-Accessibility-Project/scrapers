import savepagenow
import os
import json
import uuid
import datetime  


def create_metadata(url, run_start):
    if not os.path.exists("schema.json"):
        print("Please create a schema.json file in the same directory as this script and fill it out with the schema generator.")
        return
    else:
        with open("schema.json", "r+", encoding="utf-8") as schema_out:
            data = json.load(schema_out)
            agency_data = data["data"]
            # Find dictionary in "data" list that matches the URL
            dataset_id = next((item for item in agency_data if item["url"] == url))
            dataset_id = dataset_id["dataset_id"]
            # Check if archives exists in the file
            if "archives" in data:
                archives = data["archives"]
            else:
                data["archives"] = []
                archives = data["archives"]
            archives.append({
                "dataset_id": dataset_id, 
                "run_start": run_start,
                "run_end": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
                "dataset_snapshot": savepagenow.capture_or_cache(url)[0]
                })
            schema_out.seek(0)
            json.dump(data, schema_out, indent=4)