import os.path
import re
from Person import Person
import json


class IOHandler:
    __jsonInput = []
    jsonPersons = []
    __script_dir = os.path.dirname(__file__)
    __pic_dir = "data_pictures/"
    __json_rel_in_path = "data_json/datas.json"
    __json_rel_out_path = "data_json/datas_out.json"

    def abs_json_path_creator(self, file_rel_path):
        return os.path.join(self.__script_dir, file_rel_path)

    def abs_pic_path_creator(self, file_name):
        return os.path.join(self.__script_dir, self.__pic_dir+file_name)


    def __init__(self):
        if len(IOHandler.jsonPersons) < 1:
            self.__input_handler()

    def __input_handler(self):
        inputFile = open(self.abs_json_path_creator(self.__json_rel_in_path))
        self.___jsonInput = json.load(inputFile)
        for row in self.___jsonInput:
            IOHandler.jsonPersons.append(Person(
                identifier=row["identifier"],
                identifier_image=row["identifier_image"],
                results=row["results"],
                result_image=row["result_image"],
                confirmed_identifier=row["confirmed_identifier"],
                confirmed_results=row["confirmed_results"]
            ))

    def next_value_iterate(self, i):
        if i < (len(IOHandler.jsonPersons) - 1):
            i += 1
        return i

    def prev_value_iterate(self, i):
        if i > 0:
            i -= 1
        return i

    def string_converter(self, string_needs_converted):
        if type(string_needs_converted) is not list:
            return list(map(int, re.sub("[(|)|,]", "", string_needs_converted).split()))

    def output_handler(self):
        outputFile = open(self.abs_json_path_creator(self.__json_rel_out_path), "w")
        outputFile.write(json.dumps([o.dump() for o in IOHandler.jsonPersons], indent=4))