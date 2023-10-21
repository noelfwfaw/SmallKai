from JsonToCsv import JsonToCsv

RAWDATA_FILE = "../RawData/ship_data_statistics.json"
DATA_FILE = "../Data/ShipAttribute.csv"

BLACK_ROOT_KEY = ["all"]

DATA_SPACE_TO_WRITE = {
    "名称": "name",
    "英文名称": "english_name",
    "星级": "star",
    "Id": "id",
    "类型": "type",
    "耐久": "attrs.0",
    "炮击": "attrs.1",
    "雷击": "attrs.2",
    "防空": "attrs.3",
    "航空": "attrs.4",
    "装填": "attrs.5",
    "反潜": "attrs.6",
    "命中": "attrs.7",
    "机动": "attrs.8",
    "耐久(增长)": "attrs_growth.0",
    "炮击(增长)": "attrs_growth.1",
    "雷击(增长)": "attrs_growth.2",
    "防空(增长)": "attrs_growth.3",
    "航空(增长)": "attrs_growth.4",
    "装填(增长)": "attrs_growth.5",
    "反潜(增长)": "attrs_growth.6",
    "命中(增长)": "attrs_growth.7",
    "机动(增长)": "attrs_growth.8"
}

if __name__ == "__main__":
    JsonToCsv(RAWDATA_FILE, DATA_SPACE_TO_WRITE, BLACK_ROOT_KEY).WriteToFile(DATA_FILE)
