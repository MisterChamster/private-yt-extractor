from yt_dlp import YoutubeDL
from os     import chdir, mkdir, path
from math   import ceil
from time   import localtime, strftime
import datetime

import src.utils  as utils
import src.askers as askers



def extract_plist_data(plist_url):
    """
    Extracts data from a playlist to a file.

    Downloads a playlist dictionary, asks for round or exact viewcount and write 
    order. Depending on viewcount options, either gets it for every video from 
    playlist dictionary or downloads it for every video separately. Then, creates
    a directory with playlist name on desktop if it doesn't exist and makes a file
    inside. Inside, puts playlist data, then data of every video in order
    established earlier. In the end, puts number of errors that have occurred 
    during the extract.

    Args:
        plist_url (str): url of a playlist.
    """
    ydl_getdata = {'quiet': True,
                   'extract_flat': True,
                   'force_generic_extractor': True}
    desktop_path = path.join(path.expanduser("~"), "Desktop")
    try:
        with YoutubeDL(ydl_getdata) as ydl:
            plist_dict = ydl.extract_info(plist_url, download=False)
    except:
        if not utils.is_internet_available():
            print("Internet connection failed.\n\n")
            return
        else:
            print("Something went wrong")

    plist_title = plist_dict['title']
    dir_name = utils.char_police(plist_title)
    if dir_name == "":
        dir_name = utils.illegal_to_ascii(plist_title)
    dir_name += "_extracts"
    
    round_or_exact = askers.ask_round_or_exact()
    print()
    write_order = askers.ask_extract_write_order()
    print()
    if round_or_exact == "round":
        plist_list = [[el["url"], el["title"], el["duration"], el["view_count"]] for el in plist_dict['entries']]
    elif round_or_exact == "exact":
        plist_list = [[el["url"], el["title"], el["duration"]] for el in plist_dict['entries']] 
        try:
            for el in plist_list:
                with YoutubeDL(ydl_getdata) as ydl:
                    temp_vid_dict = ydl.extract_info(el[0], download=False)
                el.append(temp_vid_dict["view_count"])
        except:
            if not utils.is_internet_available():
                print("Internet connection failed.\n\n")
                return
            else:
                print("Something went wrong")

    # print("Data is extracted and it's almost time to write everything to a file\n")
    plist_len = plist_dict['playlist_count']

    if write_order == "asc":
        start_index = 0
        end_index   = plist_len
        first_quart = ceil(plist_len/4)
        third_quart = ceil((plist_len/4)*3)
        pop_index   = 0
    else:
        start_index = plist_len - 1
        end_index   = -1
        first_quart = ceil((plist_len/4)*3)
        third_quart = ceil(plist_len/4)
        pop_index   = -1

    halfway        = ceil(plist_len/2)
    quart_dict     = {first_quart: "One quarter down, three to go", halfway: "We're halfway there!", third_quart: "Just one more quarter..."}
    total_errors   = 0
    calendarium    = str(datetime.date.today())
    current_time   = strftime("%H:%M:%S", localtime())
    filename       = dir_name + "_extract_" + calendarium[:4] + calendarium[5:7] + calendarium[8:10] + current_time[:2] + current_time[3:5] + current_time[6:8] + write_order
    total_duration = 0

    if not path.exists(desktop_path + "/" + dir_name):
        mkdir(dir_name)
    chdir(dir_name)

    with open(filename + ".txt", "w", encoding="utf-8") as f:
        modified_date = plist_dict['modified_date']
        modified_date = modified_date[-2:] + "." + modified_date[4:6] + "." + modified_date[:4]

        for index in range(start_index, end_index, 1-2*(end_index==-1)):
            vid_data = plist_list[pop_index]
            total_duration += vid_data[2]
        time_format = str(datetime.timedelta(seconds=total_duration))

        f.write(f"Playlist name:                {plist_title}\n")
        f.write(f"Playlist's url:               {plist_dict['original_url']}\n")
        f.write(f"Playlist's owner:             {plist_dict['channel']}\n")
        f.write(f"Owner's URL:                  {plist_dict['channel_url']}\n")
        f.write(f"Playlist last updated on:     {modified_date}\n")
        f.write(f"Time of this data extract:    {calendarium}, {current_time}\n")
        f.write(f"Playlist views so far:        {utils.dots(plist_dict['view_count'])}\n")
        f.write(f"Current playlist length:      {plist_len}\n")
        f.write(f"Current videos added length:  {time_format}\n\n\n\n")
        print("Downloading...")


        for index in range(start_index, end_index, 1-2*(end_index==-1)):
            if index in quart_dict:
                print(quart_dict.pop(index))

            vid_data = plist_list[pop_index]
            try:
                f.write(f"{index + 1}. {vid_data[1]}\n")
                f.write(f"Views: {utils.dots(vid_data[3])}\n")
                f.write(f"{vid_data[0]}\n\n") #URL
            except:
                total_errors += 1
                f.write(f"{plist_len - index}. An error has occurred when trying to download data of a video with URL: {vid_data[0]}\n\n")
            plist_list.pop(pop_index)

        if total_errors == 0:
            f.write("\n\n\n\n\nNo errors have occurred during extraction")
        else:
            f.write(f"\n\n\n\n\nNumber of errors during extraction: {total_errors}")
        f.write("\n")
    
    print("\n" + plist_title + " data has been successfully extracted to Your desktop!")
    if total_errors == 0:
        print("No errors have occurred during extraction")
    else:
        print(f"Number of errors during extraction: {total_errors}")
