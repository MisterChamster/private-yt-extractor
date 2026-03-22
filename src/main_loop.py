import os
from pathlib import Path

import src.utils         as utils
import src.askers        as askers
import src.extract_tools as extracts



proj_path = Path(__file__).resolve().parent
extracted_dir_path = proj_path / "extracted"
print(extracted_dir_path)

def main_loop() -> None:
    while True:
        print()
        print("======================================================\n"
              "============== Welcome to yt extractor! ==============\n"
              "======================================================\n")
        os.chdir(extracted_dir_path)
        url = askers.ask_url()

        if not url:
            return
        if utils.is_url_playlist(url):
            print()
            extracts.extract_plist_data(url)
        else:
            print("Invalid input!\n\n")
