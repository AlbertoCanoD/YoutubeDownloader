from pytube import YouTube
from progress_bar import progress_function


# Ask for the link
#link = input("Enter the link of YouTube audio you want to download: ")
link = "https://www.youtube.com/watch?v=uVl9C3d7ySY"
yt = YouTube(link, on_progress_callback=progress_function)

blue = '\033[38;2;173;216;230m'  # Hex ADD8E6
red = '\033[38;2;255;105;97m'  # Hex FF6961
reset = '\033[39m'  # Reset terminal color

print(blue + "Title: ", yt.title, "\nChannel: ", yt.author,  "\nLength: ",
      yt.length, "s", "\nViews: ", yt.views)
print(red + "\nSelect the audio stream.\n↳" + reset)

try:
    audio_filter = yt.streams.filter(only_audio=True)  # Filter only audio streams
    audio_streams = list(enumerate(audio_filter))  # List of audio streams
except:
    print("Audio streams not found")

for audio_stream in audio_streams: # Printing all audio streams
    print(audio_stream)

option = int(input("\nSelect the desired stream: "))
download = audio_streams[option]
# print(descarga)
# descarga.download()
# listVidAud.extend(listAud)
# descarga.download()
#numero = listVidAud[opcion]
# numero.download()

#st = yt.streams.get_by_itag(listVidAud[opcion])
# st.download
# To download
# Para descargar
# dn_video.download()
# try:
#   descarga.download()
#  print("Descarga correcta")
# except:
#   print("Error en la descarga")
# if dn_video.download():
#   print("Descarga correcta")
#print("Error en la descarga")
