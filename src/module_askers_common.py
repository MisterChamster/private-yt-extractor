def ask_url():
    print("Enter URL: \n>> ", end="")
    url = str(input())
    if '&list=' in url:
        url = url[:url.find('&list=')]
    return url


def ask_plist_action():
    while True:
        print("Choose playlist option:\n" \
              "Enter - download\n" \
              "e     - extract playlist data\n\n>> ", end="")
        action = str(input())

        if action not in ["", "e"]:
            print("Incorrect input.\n")
        elif action == "":
            return "download"
        elif action == "e":
            return "extract"


def ask_save_ext():
    """
    Asks user for extension.

    In infinite loop, forces user to input either 4, 3 or f 
    to get proper extension.

    Returns:
        str: Extenstion chosen by user.
    """
    user_input = " "
    format_dict = {"4": "mp4", "3": "mp3", "f": "flac"}
    while user_input not in format_dict:
        user_input = input("What format do You want to save as? (4 - mp4, 3 - mp3, f - flac)\n>> ").lower()

    return format_dict[user_input]
