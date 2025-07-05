import os
from .module_askers import ask_url
from .module_big_routes import extract_plist_data
from .module_utils import determine_url_type



def main_loop():
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        print()
        url = ask_url()
        url_type = determine_url_type(url)

        if url_type == 'plist':
            print()
            extract_plist_data(url)
        else:
            print("Invalid input!\n")

        again = " "
        while again not in ["", "y", "e"]:
            again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
        if again == "e":
            break
