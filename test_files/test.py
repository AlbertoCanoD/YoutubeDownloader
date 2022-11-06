#Import pytube
from pytube import YouTube

#Enter the link
link = input("Link del video: ")

#yt is a object of YouTube class
yt = YouTube(link)

#Try to get the title, lenght and author of the video
#Intentamos obtener el titulo, longitud y autor del video
try:
    print("\nTitulo: ", yt.title, "\nDuracion: ", yt.length, " segundos", "\nCanal: ", yt.author)
except:
    print("Intentelo de nuevo, revise el link.")

#Video and audio
try:
    videoAudio = yt.streams.filter(progressive=True)
    listVidAud = list(enumerate(videoAudio))
except:
    print("No hay pistas de Video y Audio")

#Print the list of video and audio 
print("\nVideo y Audio")
for a in listVidAud:
    print(a)

#Only audio
try:
    audio = yt.streams.filter(only_audio=True)
    #List of audio, start in 1, only have 1 progressive stream
    listAud = list(enumerate(audio, 1))
except:
    print("No hay pistas de Audio")

#Print the list of audio
print("\nAudio")
for b in listAud:
   print(b)

#List union to get all streams
#Union de la lista 
#listVidAud.extend(listAud)
#listaAll = listVidAud + listAud
#print("\n")
#for b in listaAll:
#   print(b)


#Format of list
#Formato de la lista
#allVA = yt.streams.filter(progressive=True, only_audio=True)
tot = videoAudio + audio 
listAllVA = list(enumerate(allVA))
for a in listAllVA:
    print(a)

listVidAud.extend(listAud)

for a in listVidAud:
    print(a)
#https://www.youtube.com/watch?v=vOL40lrhE6U

print("\nElige el formato deseado")
opcion = int(input("Opcion: "))
descarga = allVA[opcion]
print(descarga)
descarga.download()
listVidAud.extend(listAud)
#descarga.download()
#numero = listVidAud[opcion]
#numero.download()

#st = yt.streams.get_by_itag(listVidAud[opcion])
#st.download
#To download
#Para descargar
#dn_video.download()
#try:
 #   descarga.download()
  #  print("Descarga correcta")
#except:
 #   print("Error en la descarga")
#if dn_video.download():
 #   print("Descarga correcta")
#print("Error en la descarga")

#https://www.youtube.com/watch?v=vOL40lrhE6U