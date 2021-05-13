#Importamos pytube
from pytube import YouTube

#Introducimos el link
link = input("Link del video: ")
yt = YouTube(link)

#Mostramos todas las opciones de descarga posible
#videos = yt.streams.all()
#videos = yt.streams.filter(progressive=True)
videos = yt.streams.filter(only_audio=True)
#Formato de la lista
video =list(enumerate(videos))

#Imprimir los resultados
for i in video:
    print(i)

print("Elige el formato deseado")
dn_option = int(input("Opcion: "))
dn_video = videos[dn_option]
#Para descargar
dn_video.download()#Mostramos todas las opciones de descarga posible

print("Descarga correcta")