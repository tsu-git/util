#!/usr/bin/python
import re

def find_attr(attribute_name, object_name):
    for attr in dir(object_name):
        if match := re.search(attribute_name, attr):
            print(attr)
