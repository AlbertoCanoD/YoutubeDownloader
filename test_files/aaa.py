from pytube import YouTube
from pytube.cli import on_progress

fuchsia = '\033[38;2;255;00;255m'  # color as hex #FF00FF
reset_color = '\033[39m'

# url is url of youtube video to download.


def download_youtube(url):
    """ Instantiates YouTube class and downloads selected video.  Uses Built-in
    pytube.cli function on_progress to show a DOS style progress bar. """
    yt = YouTube(url, on_progress_callback=on_progress)

    # following line displays title and number of times video has been viewed.
    print(f'\n' + fuchsia + 'Downloading: ', yt.title, '~ viewed', yt.views,
          'times.')

    # creates download and downloads to subdirectory called 'downloads'
    yt.streams.first().download('.\\downloads\\')

    # displays message verifying download is complete, and resets color scheme
    # back to original color scheme.
    print(f'\nFinished downloading:  {yt.title}' + reset_color)


url = "https://www.youtube.com/watch?v=XuhGPLhph0s"

download_youtube(url)
