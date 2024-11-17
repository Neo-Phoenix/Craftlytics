import json
from pathlib import Path

cwd = Path.cwd()

def getJsonsPath():
    recipes = cwd.joinpath('recipes')
    return recipes

def getJsonsPathAsList():
    files = []
    for file in Path(getJsonsPath()).glob("*.json"):
        files.append(file)
    return files

def loadJsons():
    jsons = []
    for filepath in getJsonsPathAsList():
        with open(filepath, "r") as file:
            recipeObject = json.load(file)
            jsons.append(recipeObject)
    return jsons
        
