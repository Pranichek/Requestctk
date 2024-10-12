import json, os

def read_json(filename:str):
    path_to_phile = os.path.abspath(__file__ + f"/../../static/{filename}")
    with open(path_to_phile , "r" , encoding="utf-8") as file:
        return json.load(file)