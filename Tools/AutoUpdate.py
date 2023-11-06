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
REPOSITORY_ROOT_PATH = "../"
COMMIT_MESSAGE = "Upd(auto): ship data"
REPOSITORY = git.Repo(REPOSITORY_ROOT_PATH)


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

COMMIT_FILE = [
    "../RawData/ship_data_by_type.json",
    "../RawData/ship_data_statistics.json",
    "../RawData/ship_data_template.json",
    "../Data/ShipAttribute.csv",
    "../Data/ShipType.csv"
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
        remote.pull()


def Commit():
    REPOSITORY.index.add(items=[os.path.abspath(i) for i in COMMIT_FILE])
    REPOSITORY.index.commit(COMMIT_MESSAGE)


def Push():
    remote = REPOSITORY.remote()
    remote.push()


def main():
    CheckRepository()
    RedirectFile()
    ShipAttribute.main()
    ShipType.main()
    Commit()
    Push()


if __name__ == "__main__":
    main()
