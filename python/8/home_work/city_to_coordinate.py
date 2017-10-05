#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Script for html parsing static webpage: erichware.info/sposob/geograf/geogorod.htm.
    Creates nested dict in format:
    {Country: {
            Some_city: [latitude, longitude],
            other_city: [latitude, longitude]
            }
    }
"""

import collections
import re


__author__ = "Victor Klimov"
__copyright__ = "Creative Commons License"


city_pattern = re.compile(r"<option value=\"(.+)\">(.+)")
country_patter = re.compile(r"<optgroup label=\"(.+)\">")

d = collections.defaultdict(dict)
saved_country = ""
flag = False
path = "./coordinates/raw_cities"
with open(path, "r") as f:
    for line in f:
        country = country_patter.findall(line)
        city = city_pattern.findall(line)
        if country:
            saved_country = country[0]
        if saved_country and city and not country:
            coord = city[0][0].replace("+", "").split(",")
            if len(coord) != 2:
                continue
            d[saved_country][city[0][1]] = coord


print(d["Россия"])
