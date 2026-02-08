def ask_url() -> str | None:
    while True:
        print("Enter playlist URL to extract data from:\n"
            "(to exit input 'exit')\n>> ", end="")
        asker = input().strip()

        if asker == "exit":
            return

        elif not "?list" in asker:
            print("Invalid link!\n\n")

        else:
            if '&list=' in asker:
                url = asker[:asker.find('&list=')]
            return url


def ask_round_or_exact() -> str:
    """
    Asks user if extracted video views should be exact or rounded.

    Returns:
        str: "round" or "exact".
    """
    returns_dict = {"r": "round", "e": "exact"}

    print("Choose view count type (exact values will take more time):\n"
          "r - Rounded\n"
          "e - Exact\n>> ", end="")
    asker = input().strip().lower()

    if asker in returns_dict:
        return returns_dict[asker]


def ask_extract_write_order() -> str:
    """
    Asks user for extract order.

    Returns:
        string: "asc" or "desc".
    """
    returns_dict = {
        "a": "asc",
        "d": "desc"}

    while True:
        print("Choose order of writing elements to file:\n"
              "a - Ascending\n"
              "d - Descending\n>> ", end="")
        asker = input().strip().lower()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n\n")
