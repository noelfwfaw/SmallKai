from JsonToCsv import JsonToCsv

RAWDATA_FILE = "../RawData/ship_data_statistics.json"
DATA_FILE = "../Data/ShipData.csv"

BLACK_ROOT_KEY = []

DATA_SPACE_TO_WRITE = {
    "名称": "name",
    "星级": "star",
    "Id": "id",
    "舰船类型": "type"
}


if __name__ == "__main__":
    JsonToCsv(RAWDATA_FILE, DATA_SPACE_TO_WRITE, BLACK_ROOT_KEY).WriteToFile(DATA_FILE)
