import json


def readJson(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
        print(data)
