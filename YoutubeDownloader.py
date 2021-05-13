#Import pytube
#Importamos pytube
from pytube import YouTube

#Introducimos el link
#Enter the link
link = input("Link del video: ")
yt = YouTube(link)

#We show all possible download options
#Mostramos todas las opciones de descarga posible
videos = yt.streams.all()
#videos = yt.streams.filter(progressive=True)
#videos = yt.streams.filter(only_audio=True)

#Format of list
#Formato de la lista
video =list(enumerate(videos))

#Print video results
#Imprimir los resultados de videos
for i in video:
    print(i)

print("Elige el formato deseado")
dn_option = int(input("Opcion: "))
dn_video = videos[dn_option]

#To download
#Para descargar
dn_video.download()
if dn_video.download():
    print("Descarga correcta")
print("Error en la descarga")