import os
from .module_askers import ask_url
from .module_extract import extract_plist_data
from .module_utils import is_url_playlist



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
