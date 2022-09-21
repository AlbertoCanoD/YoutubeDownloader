from pytube import YouTube

#Ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Downloading
print("Downloading...")
ys.download()
print("Download completed!!")