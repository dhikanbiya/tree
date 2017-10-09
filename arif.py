""" Modul Percobaan """

import json
import sys
from pprint import pprint
from zss import simple_distance, Node

def json_open(file):
    """ load json """
    with open(file) as json_file:
        return json.load(json_file)

def recursive(node, obj, debug):
    """ recursive json """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, list):
                if debug: print("dict_list -> {0} - {1}".format(k, v))
                newnode = node.addkid(Node("{0}".format(k)))
                recursive(newnode, v, debug)
            elif isinstance(v, dict):
                if debug: print("dict_dict -> {0} - {1}".format(k, v))
                newnode = node.addkid(Node("{0}".format(k)))
                recursive(newnode, v, debug)
            else:
                if debug: print("dict_kid -> {0} - {1}".format(k, v))
                node.addkid(Node("{0} - {1}".format(k, v)))
    elif isinstance(obj, list):
        for item in obj:
            if debug: print("list -> {0}".format(item))
            recursive(node, item, debug)

if __name__ == "__main__":
    JSON = json_open(sys.argv[1])
    root = Node("root")
    
    recursive(root, JSON, True)
    print("\n", root, sep="")