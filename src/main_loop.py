import os
from src.askers import ask_url
from src.extract_tools import extract_plist_data
from src.utils import is_url_playlist



def main_loop():
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        print()
        print("======================================================")
        print("============== Welcome to yt extractor! ==============")
        print("======================================================\n")
        url = ask_url()

        if not url:
            return
        if is_url_playlist(url):
            print()
            extract_plist_data(url)
        else:
            print("Invalid input!\n\n")
