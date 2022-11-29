from tkinter import *  # Tk, Label, Button
import webbrowser


class YoutubeDownloader:
    def __init__(self, root):
        self.master = root

        #Title and icon
        self.master.title("YoutubeDownloader")
        self.master.iconphoto(True, PhotoImage(file="icon.png"))

        # Window options
        self.master.geometry("600x400")
        self.master.minsize(width=600, height=400)
        self.master.resizable(width=True, height=False)
        self.master.update()

        # Widgets
        self.mode = StringVar(self.master)
        self.mode.set("XX + DD")

        # 1) Menu
        self.menu = OptionMenu(self.master, self.mode, "AA", "BB", "CC")

        '''menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Settings')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        helpmenu = Menu(menu)
        menu.add_cascade(label='About me', menu=helpmenu)
        helpmenu.add_command(label='My GitHub')'''

        # 2) Link box

        # 3) Download button

    def about_me():
        command = webbrowser.open(
            "https://github.com/AlbertoCanoD")


'''# Link box
    Label(self.root, text='Enter the link').grid(row=8)
    link_entry = Entry(self.root)
    link_entry.grid(row=8, column=1)

    def greet(self):
        print("Greetings!")

# Download button
    download_button = Button(
        master, text="Download", width=25, command=greet)
    download_button.pack()'''


def main():
    root = Tk()
    YoutubeDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()
