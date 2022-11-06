import sys


def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    current = ((size - bytes_remaining)/size)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(
        bar=status, percent=percent))
    sys.stdout.flush()
