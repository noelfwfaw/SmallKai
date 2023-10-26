from pathlib import Path

import git
import os
import ShipAttribute
import ShipType
from dataclasses import dataclass
import shutil

AZUR_LANE_DATE_REPOSITORY_URL = "https://github.com/AzurLaneTools/AzurLaneData"
AZUR_LANE_DATE_ROOT_PATH = "../AzurLaneData"
RAWDATA_PATH = "../RawData"

@dataclass
class FileRedirect:
    file: str
    origin: str
    redirect: str


REDIRECT_LIST = [
    FileRedirect("ship_data_by_type.json", "../AzurLaneData/CN/ShareCfg", RAWDATA_PATH),
    FileRedirect("ship_data_statistics.json", "../AzurLaneData/CN/sharecfgdata", RAWDATA_PATH),
    FileRedirect("ship_data_template.json", "../AzurLaneData/CN/sharecfgdata", RAWDATA_PATH)
]


def RedirectFile():
    for i in REDIRECT_LIST:
        shutil.copy(Path(i.origin) / i.file, Path(i.redirect))


def CheckRepository():
    if not os.path.exists(AZUR_LANE_DATE_ROOT_PATH):
        git.Repo.clone_from(url=AZUR_LANE_DATE_REPOSITORY_URL, to_path=AZUR_LANE_DATE_ROOT_PATH)
    else:
        repo = git.Repo(AZUR_LANE_DATE_ROOT_PATH)
        remote = repo.remote()
        remote.fetch()


def main():
    CheckRepository()
    RedirectFile()
    ShipAttribute.main()
    ShipType.main()


if __name__ == "__main__":
    main()
