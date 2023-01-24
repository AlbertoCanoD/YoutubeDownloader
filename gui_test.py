from tkinter import *  # Tk, Label, Button
import webbrowser


class YoutubeDownloaderGUI:
    def __init__(self, root):
        self.master = root

        #Title and icon
        self.master.title("YoutubeDownloader")
        self.master.iconphoto(True, PhotoImage(file="icon.png"))

        # Window options
        self.master.geometry("600x400")
        self.master.minsize(width=600, height=400)
        self.master.resizable(width=True, height=True)
        self.master.update()



        # Widgets
        self.mode = StringVar(self.master)
        self.mode.set("Video + Audio")



        # 1) Settings
        self.menu = OptionMenu(self.master, self.mode, "AA", "BB", "CC")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='App', menu=filemenu)
        filemenu.add_command(label='Settings')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)

        #2)Link entry
        self.link_text = Label(text="Enter the link")
        self.link_scroll = Scrollbar(self.master,orient="horizontal")
        self.link_entry = Entry(self.master,font="Sans_Serif 12",xscrollcommand=self.link_scroll.set)
        self.link_scroll.config(command=self.link_entry.xview)

        #3)Selector menu

        self.mode_menu = OptionMenu(self.master,self.mode,"Video + Audio","Audio Only","Best Resolution")
        self.mode_menu.config(width=12)

        self.mode_label = Label(self.master,text="Mode:",font="Sans_Serif 10")

        self.status_label = Label(self.master,text="Ready",font="Sans_Serif 12",padx=10,relief="sunken")

        self.link_entry_button = Button(
            self.master,
            text="Submit",
            width=15,
            #command=self.submit
        )

        self.dir_entry_x_scroll = Scrollbar(
            self.master,
            orient="horizontal"
        )

        self.dir_entry = Entry(
            self.master,
            font="Sans_Serif 12",
            xscrollcommand=self.dir_entry_x_scroll.set
        )

        self.dir_entry_x_scroll.config(command=self.dir_entry.xview)

        self.dir_entry_button = Button(
            self.master,
            text="Select Directory",
            width=15,
            #command=self.dir_select
        )

        #HQ mode widgets:
        self.stream_list_y_scroll = Scrollbar(
            self.master,
            orient="vertical"
        )

        self.stream_list = Listbox(
            self.master,
            yscrollcommand=self.stream_list_y_scroll.set
        )

        self.stream_list_y_scroll.config(command=self.stream_list.yview)
        self.stream_selection = StringVar(self.master)

        #Layout:
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(5, weight=1)

        self.link_text.grid(row=0,column=0,sticky="n") #Link text

        self.link_entry.grid(row=1, column=0, sticky="ew") #Link entry
        self.link_scroll.grid(row=2, column=0, sticky="ew") #Link entry scrollbar

        self.link_entry_button.grid(row=0, column=1)
        self.mode_label.grid(row=1, column=1, sticky="ew")
        self.mode_menu.grid(row=2, column=1)
        self.status_label.grid(row=3, column=0)
        self.dir_entry.grid(row=4, column=0, sticky="ew")
        self.dir_entry_x_scroll.grid(row=5, column=0, sticky="ew")
        self.dir_entry_button.grid(row=3, column=1)    

        #Bindings, Traces, Protocols:
        #self.link_entry.bind("<Return>", self.submit)
        #self.stream_list.bind("<Return>", self.update_stream_selection)
        #self.stream_list.bind("<Double-Button-1>", self.update_stream_selection)
        #self.mode.trace("w", self.set_gui)
        #self.master.bind("<Control-w>", self.close)
        #self.master.protocol("WM_DELETE_WINDOW", self.close)

        #Probe ffmpeg:
        '''self.ffmpeg = which("ffmpeg")
        if not self.ffmpeg:
            messagebox.showwarning(
                "Error", 
                "Unable to probe ffmpeg.\n\n"\
                "HQ & Audio Only most likely will not function "\
                "correctly without ffmpeg.exe on the system path."
            )
            self.mode_menu.config(state="disabled")'''


        #GitHub link
        '''def callback(url):
            webbrowser.open_new_tab(url)

        link = Label(self.master, text="My GitHub profile",font=('Sans_Serif', 10), fg="gray", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e:
        callback("https://github.com/AlbertoCanoD"))'''
        

        # 2) Link box

        # 3) Download button


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
    YoutubeDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
