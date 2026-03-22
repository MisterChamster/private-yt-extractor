import os
from pathlib import Path

import src.utils         as utils
import src.askers        as askers
import src.extract_tools as extracts



proj_path = Path(__file__).resolve().parent
save_dir_path = proj_path / "extracted"
print(save_dir_path)

def main_loop() -> None:
    while True:
        print()
        print("======================================================\n"
              "============== Welcome to yt extractor! ==============\n"
              "======================================================\n")
        url = askers.ask_url()
        if not url:
            return

        cleaned_url = utils.clean_url(url)
        if cleaned_url != url:
            url = cleaned_url
            print("Your link has been cleaned of fluff.")

        if utils.is_url_playlist(url):
            print()
            extracts.extract_plist_data(url, save_dir_path)
            print()
        else:
            print("Invalid input!\n\n")
