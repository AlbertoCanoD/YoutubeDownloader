from pytube import YouTube

#Ask for the link from user
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link, on_progress_callback=progress_func)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("progress_func",)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Downloading
print("Downloading...")
ys.download()
print("Download completed!!")