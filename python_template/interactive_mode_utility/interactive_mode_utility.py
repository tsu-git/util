#!/usr/bin/python
import re

def find_attr(attribute_name: str, object_name: str):
    """find attribute in the object
    
        Attribute_name needs quatation. object_name is an imported module name
    """
    for attr in dir(object_name):
        if match := re.search(attribute_name, attr):
            print(attr)
