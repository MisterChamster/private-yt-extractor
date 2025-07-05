import os
from .module_askers_common import (ask_url,
                                   ask_plist_action)
from .module_big_routes import (save_plist,
                                extract_plist_data)
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
            url_type = ask_plist_action()
            if url_type == 'download':
                print()
                save_plist(url)
            elif url_type == 'extract':
                print()
                extract_plist_data(url)
        else:
            print("Invalid input!\n")

        again = " "
        while again not in ["", "y", "e"]:
            again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
        if again == "e":
            break
