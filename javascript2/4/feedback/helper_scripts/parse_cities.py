"""
Parse cities from https://technopoint.ru/feedback/
and create json
"""
import json
import re
import sys

lst = []
file_name = sys.argv[1]
pattern = r"\<option.*?\>(.+?)\<"
with open(file_name, "r") as handle:
    for i, line in enumerate(handle):
        d = {}
        result = re.findall(pattern, line)
        if result:
            d = {"city": result[0], "id": "city_{}".format(i + 1)}
            lst.append(d)


with open("cities.json", "w") as write_handle:
    json.dump(lst, write_handle, ensure_ascii=False)
   


