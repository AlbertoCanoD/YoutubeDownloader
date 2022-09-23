import sys
from pytube import YouTube


def progress_func(stream, chunk, bytes_remaining):
    # Size of video
    size = stream.filesize
    curr = size - bytes_remaining
    done = int(50 * curr / size)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)))
    sys.stdout.flush()


# Ask for the link
link = input("Link del video: ")
yt = YouTube(link, on_progress_callback=progress_func)

try:
    print("\nTitulo: ", yt.title, "\nDuracion: ",
          yt.length, " segundos", "\nCanal: ", yt.author)
except:
    print("Intentelo de nuevo, revise el link.")

#Filter only audio streams
audio = yt.streams.filter(only_audio=True)
# List of audio streams
audioStreams = list(enumerate(audio))

print("\nAudio")
for a in audioStreams:
    print(a)

# Only audio
try:
    audio = yt.streams.filter(only_audio=True)
    # List of audio streams
    audioStreams = list(enumerate(audio))
except:
    print("No hay pistas de Audio")

# Print the list of audio
print("\nAudio")
for a in audioStreams:
    print(a)

# https://www.youtube.com/watch?v=vOL40lrhE6U

print("\nElige el formato deseado")
opcion = int(input("Opcion: "))
descarga = audioStreams[opcion]
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

# https://www.youtube.com/watch?v=vOL40lrhE6U
