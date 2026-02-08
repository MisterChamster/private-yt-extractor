import os

import src.askers        as askers
import src.extract_tools as extracts
import src.utils         as utils



def main_loop() -> None:
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        print()
        print("======================================================")
        print("============== Welcome to yt extractor! ==============")
        print("======================================================\n")
        url = askers.ask_url()

        if not url:
            return
        if utils.is_url_playlist(url):
            print()
            extracts.extract_plist_data(url)
        else:
            print("Invalid input!\n\n")
