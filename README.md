# YoutubeDownloader
A simple program developed in Python that will allow us to download videos/audio from Youtube just by entering a link. 

Installation requirements
======================

In order to run the program, it will be necessary to have a Python version equal or higher than 3.6. In addition to this, you will need to have pip installed. And also you need to install the library pytube.

About pytube
======================

pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos. You can find documentation at https://pytube.io/en/latest/index.html

Installation of python and pip
======================

Windows installation
--

To install python, you must install it from his web [www.python.org](https://www.python.org/downloads/windows/), you must choose the version that you want being greater or equal to 3.6, I recommend the last version.

Once installed, pip, which is the Python package and installation manager, is installed. To do this, first check that the Python installation is correct and its version using the command(If Python is in the system PATH, https://geek-university.com/add-python-to-the-windows-path/):

    $ py --version

To check that pip is installed, use the following command:

    $ py -m pip --version
    
To check if it is up to date:

    $ py -m pip install -U pip
    
    
Linux installation
--

### Ubuntu

Check if Python is installed:

    $ python3 --version

Otherwise:

    $ sudo apt update
    $ sudo apt upgrade
    $ sudo apt install python

### Fedora

Python is preinstalled in Fedora(https://developer.fedoraproject.org/tech/languages/python/python-installation.html).

    $ python3 --version
    
Otherwise:

    $ sudo dnf install python

### Arch Linux

Check if Python is installed, or download other version(https://wiki.archlinux.org/title/python).

    $ python3 --version
    
Otherwise:

    $ sudo pacman -S python

Installation of pytube
======================

To install pytube, run the following command in your terminal

    $ pip install pytube


TODO
======================

- CLI
    - ~~Download best video quality~~ ✅
    - ~~Download best audio quality~~ ✅
    - Implement youtube exceptions 
    - Option selector for video quality or format
- GUI
    - Paste in box with click on icon
    - Options menu
        - Select folder to save audio
        - Select folder to save video
        - Select darkmode 
    - Select format and quality for video or audio
