import platform
from pytube import YouTube
from useful_functions import progress_function, colors


# Ask for the link
#link = input("Enter the link of YouTube audio you want to download: ")
link = "https://www.youtube.com/watch?v=uVl9C3d7ySY"
yt = YouTube(link, on_progress_callback=progress_function)

'''blue = '\033[38;2;173;216;230m'  # Hex ADD8E6
red = '\033[38;2;255;105;97m'  # Hex FF6961
reset = '\033[39m'  # Reset terminal color'''

print(colors(blue) + "Title: ", yt.title, "\nChannel: ", yt.author,  "\nLength: ",
      yt.length, "s", "\nViews: ", yt.views)
print(colors(red) + "\nSelect the audio stream.\n↳" + colors(reset))

try:
    # Filter only audio streams
    audio_filter = yt.streams.filter(only_audio=True)
    audio_streams = list(enumerate(audio_filter))
except:
    print("Audio streams not found")

for audio_stream in audio_streams:  # Print all audio streams
    print(audio_stream)

option = int(input("\nSelect the desired stream: "))
selected_stream = audio_streams[option]
print("Selected stream -> " + str(selected_stream))

audio_filter.itag_index
selected_stream.index(option)

audio_select = selected_stream.index(option)

audio = yt.streams.get_by_itag(audio_select)


'''
TODO
Get the itag of selected stream
Download by itag
'''

print("Downloading video...")
if platform.system() == "Linux":
    if audio.download('~/YoutubeDownloads'):
        print("\nDownload completed!!" + reset)
    else:
        print("\nDownload error." + reset)
elif platform.system() == "Windows":
    if audio.download('/YoutubeDownloads'):
        print("\nDownload completed!!" + reset)
    else:
        print("\nDownload error." + reset)
