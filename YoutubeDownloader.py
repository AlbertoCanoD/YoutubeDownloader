#Import pytube
from pytube import YouTube

#Enter the link
link = input("Link del video: ")
yt = YouTube(link)

#Store all possible download options
videos = yt.streams.all()

#List Download options
#Opciones de descarga con sus listas
listVid = list(enumerate(videos))

#Print the resuls
for i in listVid:
    print(i)

print("Elige el formato deseado")
opcion = int(input("Opcion: "))
descarga = listVid[opcion]

#Download
try:
    descarga.download()
    print("Descarga correcta")
except:
    print("Error en la descarga")
