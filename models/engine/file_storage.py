#!/usr/bin/env python3
"""serializes and deserializes objects to
and from json
"""

import json


class FileStorage:
    """defined a class to serialize and
    deserialize json
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes from a json file
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
               FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
