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

#Download options with their lists
#Opciones de descarga con sus listas
listVid = list(enumerate(videos))

#Print video results
#Imprimir los resultados
for i in listVid:
    print(i)

print("Elige el formato deseado")
opcion = int(input("Opcion: "))
descarga = listVid[opcion]

#To download
#Para descargar
try:
    descarga.download()
    print("Descarga correcta")
except:
    print("Error en la descarga")
