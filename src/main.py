"""
    ##########################
    #   Youtube Downloader   #
    ##########################
"""

# import pytube 
from pytube import YouTube

# initialized some color
cyan_color = "\033[1;36;40m"
green_color = "\033[1;32;40m"
yellow_color = "\033[1;33;40m"
white_color = "\033[1;37;40m"

# cli logo
print("\033c")
print(green_color + "  _______________________________")
print(green_color + " |                               |")
print(green_color + " |    " + cyan_color + "          __         "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "         |  |        "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "         |  |        "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "       __|  |__      "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "       \      /      "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "        \    /       "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "         \  /        "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "          \/         "+ green_color + "      | ")
print(green_color + " |    " + cyan_color + "                     "+ green_color + "      | ")
print(green_color + " |_______________________________| \n" + white_color)

print(green_color + " =============" + cyan_color + " GetYou " + green_color + "=============" + white_color)

# get user input youtube link
video_url = input(cyan_color + " Enter you're yotube video link here : " + white_color)
youtube_video = YouTube(video_url)

# video resolution
high_res = youtube_video.streams.get_highest_resolution()
low_res = youtube_video.streams.get_lowest_resolution()

# mark video info
print(green_color + " \n =============" + cyan_color + " VidInfo " + green_color + "============" + white_color)

# all about video information
print(yellow_color + " Video Title -> " + green_color + youtube_video.title)
print(yellow_color + " Video Thumbnail -> " + green_color + youtube_video.thumbnail_url)
print(yellow_color + " Highest Resolution -> " + green_color + high_res.resolution)
print(yellow_color + " Lowest Resolution -> " + green_color + low_res.resolution)

# download video
high_res.download()

# messages finished
print(green_color + " Download Finished." + white_color)