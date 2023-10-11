import csv
import json
from typing import Union, Any

class JsonToCsv:
    def __init__(self, JsonFile, Space: dict, BlackRootKey: list[str] = list()):
        self.File = JsonFile
        self.DataSpace = Space
        self.BlackRootKey = BlackRootKey
        with open(JsonFile, mode="r", encoding="utf-8") as f:
            self.Data: dict = json.load(f)

    def __FormatNode(self, Node: Union[str, list[str, int]]) -> list[str, int]:
        Result = []
        if isinstance(Node, str):
            Result = Node.split(".")
        elif isinstance(Node, list):
            Result = Node
        return Result

    def GetDataThroughNode(self, Node: Union[str, list[str, int]]) -> Any:
        NodeList = self.__FormatNode(Node)
        Result = self.Data
        for i in NodeList:
            if isinstance(Result, dict):
                Result = Result[str(i)]
            elif isinstance(Result, list):
                Result = Result[int(i)]
        return Result

    def WriteToFile(self, File):
        with open(File, mode="w", encoding="utf-8", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerow(self.DataSpace.keys())
            Writer.writerows(
                [[self.GetDataThroughNode(".".join([Key, Node])) for Node in self.DataSpace.values()] for Key in self.Data.keys() if Key not in self.BlackRootKey])