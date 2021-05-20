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

#Only audio
try:
    audio = yt.streams.filter(only_audio=True)
    #List of audio streams
    listAud = list(enumerate(audio))
except:
    print("No hay pistas de Audio")

#Print the list of audio
print("\nAudio")
for a in listAud:
   print(a)

#https://www.youtube.com/watch?v=vOL40lrhE6U

print("\nElige el formato deseado")
opcion = int(input("Opcion: "))
descarga = listAud[opcion]
#print(descarga)
#descarga.download()
#listVidAud.extend(listAud)
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