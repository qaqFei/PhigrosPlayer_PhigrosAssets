from os import listdir
from os.path import isfile
from json import dump

def searchFolder(p: str):
    result = {"files": [], "folders": []}
    items = listdir(p)
    for item in items:
        itemp = f"{p}/{item}"
        if isfile(itemp):
            result["files"].append({"filePath": itemp[len(assetsPath):], "downloadPath": itemp})
        else:
            result["folders"].append(itemp[len(assetsPath):])
            folderTree = searchFolder(itemp)
            result["files"].extend(folderTree["files"])
            result["folders"].extend(folderTree["folders"])
    return result

assetsPath = input("assets path: ")
folderTree = searchFolder(assetsPath)
dump(
    folderTree,
    open(input("output file: "), "w", encoding="utf-8"),
    indent = 4,
    ensure_ascii = False
)