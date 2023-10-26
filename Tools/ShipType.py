from JsonToCsv import JsonToCsv

RAWDATA_FILE = "../RawData/ship_data_by_type.json"
DATA_FILE = "../Data/ShipType.csv"

BLACK_ROOT_KEY = ["all"]

DATA_SPACE_TO_WRITE = {
    "类型": "type_name",
    "Id": "ship_type",
    "TeamId": "team_type"
}


def main():
    JsonToCsv(RAWDATA_FILE, DATA_SPACE_TO_WRITE, BLACK_ROOT_KEY).WriteToFile(DATA_FILE)


if __name__ == "__main__":
    main()
