import os
from pprint import pprint


def get_zip_file(input_path):
    result_path = []
    for file in os.listdir(input_path):
        result_path.append(os.path.join(input_path, file))
        if os.path.isdir(os.path.join(input_path, file)):
            result_path.extend(get_zip_file(os.path.join(input_path, file)))
    return result_path


ls = get_zip_file(os.getcwd())

ls.sort()

pprint(ls, width=120, compact=True)