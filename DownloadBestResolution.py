import sys
from pytube import YouTube


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)))
    sys.stdout.flush()


# Ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link, on_progress_callback=progress_func)

blue = '\033[38;2;173;216;230m'  # Hex ADD8E6
red = '\033[38;2;255;105;97m'  # Hex FF6961
reset_color = '\033[39m'

print(blue + "Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "s")

# Getting the highest resolution possible
print(red + "Selecting the highest resolution.")
ys = yt.streams.get_highest_resolution()

# Downloading
print("Downloading video...")
if ys.download():
    print("\nDownload completed!!" + reset_color)
else:
    print("\nDownload error." + reset_color)
