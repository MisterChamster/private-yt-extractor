import os
from .module_askers import ask_url
from .module_extract import extract_plist_data
from .module_utils import is_url_playlist



def main_loop():
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        print()
        url = ask_url()
        if is_url_playlist(url):
            print()
            extract_plist_data(url)
        else:
            print("Invalid input!\n")

        again = " "
        while again not in ["", "y", "e"]:
            again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
        if again == "e":
            break
