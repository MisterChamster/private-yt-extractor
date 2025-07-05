def ask_url():
    print("Enter URL: \n>> ", end="")
    url = str(input())
    if '&list=' in url:
        url = url[:url.find('&list=')]
    return url
