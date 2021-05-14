#Import pytube
#Importamos pytube
from pytube import YouTube

#Introducimos el link
#Enter the link
link = input("Link del video: ")
yt = YouTube(link)

print("Titulo: ", yt.title, "\nDuracion: ", yt.length, " segundos", "\nCanal: ", yt.author)
#We show all possible download options
#Mostramos todas las opciones de descarga posible
#videos = yt.streams.all()
#videos = yt.streams.filter(progressive=True)
#videos = yt.streams.filter(only_audio=True)

#Download options with their lists
#Opciones de descarga con sus listas

#Video and audio
try:
    videoAudio = yt.streams.filter(progressive=True)
    listVidAud = list(enumerate(videoAudio))
    #break# print("Pistas de Video y Audio")
except:
    print("No hay pistas de Video y Audio")

#Only audio
try:
    audio = yt.streams.filter(only_audio=True)
    listAud = list(enumerate(audio, 1))
except:
    print("No hay pistas de Audio")

#Format of list
#Formato de la lista
allVA = yt.streams.filter(progressive=True, only_audio=True)
listAllVA = list(enumerate(allVA.filter()))

list1 = list(enumerate(allVA.filter(progressive=True)))
list1.index




print("Video y Audio")

for a in listVidAud:
    print(a)

print("Audio")

for i in listAud:
   print(i)

#List union 
listVidAud.extend(listAud)

print("Elige el formato deseado")
dn_option = int(input("Opcion: "))
descarga = listAllVA[dn_option]

#To download
#Para descargar
#dn_video.download()
try:
    descarga.download()
    print("Descarga correcta")
except:
    print("Error en la descarga")
#if dn_video.download():
 #   print("Descarga correcta")
#print("Error en la descarga")

#https://www.youtube.com/watch?v=vOL40lrhE6U