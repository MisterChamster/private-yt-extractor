def ask_url():
    print("Enter playlist URL to extract data from:\n" \
          "(to exit input 'exit')\n" \
          ">> ", end="")
    url = str(input())
    if '&list=' in url:
        url = url[:url.find('&list=')]
    return url


def ask_round_or_exact():
    """
    Asks user if extracted video views should be exact or rounded.

    Returns:
        str: "round" or "exact".
    """
    input_RE = " "
    RE_dict = {"r": "round", "e": "exact"}
    print("Choose view count type (exact values will take more time):\n" \
          "r - rounded\n" \
          "e - exact\n\n>> ", end="")
    input_RE = str(input())

    if input_RE in RE_dict:
        return RE_dict[input_RE]


def ask_extract_write_order():
    """
    Asks user for extract order.

    Returns:
        string: "asc" or "desc".
    """
    result_dict = {"a": "asc",
                   "d": "desc"}

    while True:
        print("Choose order of writing elements to file:\n" \
              "a - Ascending\n" \
              "d - Descending\n\n>> ", end="")
        asker = input()

        if asker in result_dict:
            return result_dict[asker]
        else:
            print("Incorrect input.\n\n")
