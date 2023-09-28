import csv
import json


class JsonToCsv:
    def __init__(self):
        self.RawDataFile = str()
        self.RawData = dict()

        self.ProcessedData = list()

        self.DataSpace = dict()

    class Data:
        def __init__(self, dict_):
            self.__dict__.update(dict_)

        def Get(self, name):
            return self.__getattribute__(name)

    def LoadFile(self, File):
        self.RawDataFile = File
        self.RawData = self.__LoadRawData(self.RawDataFile)
        self.ProcessedData = self.__ProcessData(self.RawData)
        return self

    def SetDataSpace(self, Space: dict):
        self.DataSpace = Space
        return self

    def WriteToFile(self, File):
        self.__WriteToFile(self.ProcessedData, File)

    def __LoadRawData(self, File) -> dict:
        with open(File, mode="r", encoding="utf-8") as f:
            return json.load(f)

    def __DictToObject(self, Dict: dict) -> Data:
        return json.loads(json.dumps(Dict), object_hook=JsonToCsv.Data)

    def __ProcessData(self, RawData: dict) -> list[Data]:
        DataList = list()
        for _, Value in RawData.items():
            DataList.append(self.__DictToObject(Value))
        return DataList

    def __WriteToFile(self, Data: list[Data], File):
        with open(File, mode="w", encoding="utf-8", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerow(self.DataSpace.keys())
            Writer.writerows(
                [[i.Get(j) for j in self.DataSpace.values()] for i in Data if isinstance(i, JsonToCsv.Data)])
