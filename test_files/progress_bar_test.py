import sys
from pytube import YouTube
from progress_bar import progress_function

# Ask for the link
link = input("Enter the link of YouTube video you want to download: ")
#link = "https://www.youtube.com/watch?v=Zyet1YI2Sl0"
yt = YouTube(link, on_progress_callback=progress_function)

blue = '\033[38;2;173;216;230m'  # Hex ADD8E6
red = '\033[38;2;255;105;97m'  # Hex FF6961
reset = '\033[39m'  # Reset terminal color

print(blue + "Title: ", yt.title, "\nChannel: ", yt.author,  "\nLength: ",
      yt.length, "s", "\nViews: ", yt.views)
print(red + "Selecting the highest resolution.")

video = yt.streams.get_highest_resolution()

# Downloading
print("Downloading video...")
if video.download():
    print("\nDownload completed!!" + reset)
else:
    print("\nDownload error." + reset)

