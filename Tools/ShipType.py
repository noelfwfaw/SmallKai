import csv
import json

from JsonToCsv import JsonToCsv

RAWDATA_FILE = "../RawData/ship_data_by_type.json"
DATA_FILE = "../Data/ShipType.csv"

DATA_SPACE_TO_WRITE = {
    "类型": "type_name",
    "Id": "ship_type",
    "TeamId": "team_type"
}

if __name__ == "__main__":
    JsonToCsv().LoadFile(RAWDATA_FILE).SetDataSpace(DATA_SPACE_TO_WRITE).WriteToFile(DATA_FILE)
