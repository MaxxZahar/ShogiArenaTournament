import shutil
import datetime
import os
from pathlib2 import Path


data_path = "../data/data.csv"
copy_path = "../data/previous"
name = {"old": "Selifonova;Aleksandra", "new": "Grishchenko;Aleksandra"}


def create_data_copy(data_path, copy_path) -> None:
    shutil.copyfile(
        data_path,
        os.path.join(
            copy_path, datetime.datetime.now().strftime("%I%M%B%d%Y") + ".csv"
        ),
    )


def change_name(name: dict, data_path, copy_path) -> None:
    create_data_copy(data_path, copy_path)
    f = Path(data_path)
    data = f.read_text()
    data = data.replace(name["old"], name["new"])
    f.write_text(data)


change_name(name, data_path, copy_path)
