"""
This script implements a process to convert the metadata obtained from a
specified S3 bucket into a structured and hierarchical JSON representation.
"""


import json


def convert_to_json(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = {}
    for line in lines:
        parts = line.strip().split("/")
        curr = data
        for part in parts:
            if part not in curr:
                curr[part] = {}
            curr = curr[part]

    json_file = open("NexRad.json", "w")
    json.dump(data, json_file, indent=6)
    json_file.close()


convert_to_json("GEOS.txt")
