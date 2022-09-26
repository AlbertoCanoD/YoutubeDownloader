import sys
from pytube import YouTube, exceptions


def progress_func(stream, chunk, bytes_remaining):
    # Size of video
    size = stream.filesize
    curr = size - bytes_remaining
    done = int(50 * curr / size)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)))
    sys.stdout.flush()


# Ask for the link
#link = input("Enter the link of YouTube video you want to download: ")
link = "https://www.youtube.com/watch?v=f9NEdDs0skM"  # Private video
yt = YouTube(link, on_progress_callback=progress_func)

blue = '\033[38;2;173;216;230m'  # Hex ADD8E6
red = '\033[38;2;255;105;97m'  # Hex FF6961
reset = '\033[39m'  # Reset terminal color

try:
    yt = YouTube(link)

except exceptions.VideoPrivate as e:
    print("Private video", e)

except exceptions.VideoUnavailable as e:
    print("Video is not found", e)

else:
    print(blue + "Title: ", yt.title, "\nChannel: ", yt.author,  "\nLength: ",
          yt.length, "s", "\nViews: ", yt.views)
    print(red + "Selecting the highest resolution.")

    try:
        # Getting the highest resolution possible
        video = yt.streams.get_highest_resolution()

    except exceptions.HTMLParseError as e:
        print(e)


# Downloading
print("Downloading video...")
if video.download():
    print("\nDownload completed!!" + reset)
else:
    print("\nDownload error." + reset)
