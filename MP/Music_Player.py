#Music Player

import customtkinter as Ctk    #For GUI
import tkinter as tk #for gui too
from tkinter import ttk        #For WidgetStyles
from tkinter import filedialog #Dialog boxes
import pygame                  #playing music
import os                      #for directory
from tkinter import messagebox #

#Main class MusicPlayer

class MusicPlayer:

    #root window(main)
    def __init__(self,root):
        self.root = root

        self.root.geometry("640x480")

        self.root.title("DTG MUSIC PLAYER")

        self.root.resizable(False,False)
        
        # self.bg_image =tk.PhotoImage(file = os.path.join(os.getcwd(),"MP","img","bg_mus.png"))
        # self.bg_label = ttk.Label(self.root, image=self.bg_image)
        # self.bg_label.place(relx=0,rely=0, relheight=1,relwidth=1)


        #style
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('.', background='black', foreground='black')
        s.configure('TFrame', background='grey',foreground='grey')
        s.configure('TButton',font=('Arial',12), background='black', foreground='grey', activebackground='brown', activeforeground='grey')
        s.configure('TLabel', font=('Arial', 12), background='black', foreground='violet')
        s.configure('Tscale', background='grey')

        #initializing pygame

        pygame.init()

        #initializing pygame mixer(

        pygame.mixer.init()
    
        #Playlist frame (Just The Frame)

        self.frame = tk.Frame(self.root)

        #Grid System
        self.frame.grid(row=0,column=0,padx=10,pady=10)

        #Playlist Listbox        #below\/the "master" is frame not root
        self.Listbox = tk.Listbox(self.frame,width=40,height=30, bg="grey")
        self.Listbox.pack(fill=tk.BOTH, expand=True)

        self.Listbox.bind("<<ListboxSelect>>", self.play_selected)

        #Control Frame (buttons et al)
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.grid(row=0,column=1,padx=10,pady=10)
        self.control_frame.configure(border=1,relief="groove",borderwidth=2)       


        #No BG image
        
        #Play/Pause button
        self.play_var = tk.StringVar() # for showing play/pause state
        self.play_var.set("Play")
        self.play_pause_button = tk.Button(self.control_frame, textvariable=self.play_var, command=self.play_pause)
        self.play_pause_button.grid(row=1,column=0,padx=10,pady=10)

        #Skip Buttons // backward

        self.backward_button = tk.Button(self.control_frame,text="⏪",command=self.skip_backward)
        self.backward_button.grid(row=2,column=0,padx=10,pady=10)

        #skip buttons // Foreward

        self.forward_button = tk.Button(self.control_frame,text="⏩",command=self.skip_forward)
        self.forward_button.grid(row=3,column=0,padx=10,pady=10)

        #Status Of Current Song // volume control

        self.status_var = tk.StringVar() 
        self.status_var.set("Volume Control")
        self.status_label = ttk.Label(self.control_frame,textvariable=self.status_var)
        self.status_label.grid(row=4,column=0,padx=10,pady=10)

        #   Volume
        self.volume_var = tk.DoubleVar()
        self.volume_scale = ttk.Scale(self.control_frame,orient="horizontal",from_=0,to=1,variable=self.volume_var,command=self.volume_set)
        self.volume_scale.grid(row=5,column=0,padx=10,pady=10)

        #Importing Music
        self.import_button = ttk.Button(self.control_frame,text="Import Music",command=self.import_music)
        self.import_button.grid(row=6,column=0,padx=10,pady=10)

        # Progress Bar"
        self.progress_bar = ttk.Progressbar(self.control_frame,orient="horizontal",length=320,mode='determinate')
        self.progress_bar.grid(row=7,column=0,padx=10,pady=10)

        #Elapsed time //prettycomplex//

        self.elapsed_time = ttk.Label(self.control_frame,text='00:00' )
        self.elapsed_time.grid(row=8,column=0,padx=10,pady=10)

        #current song label
        self.current_song = ''

        #bool to check  if song is paused or not
        self.paused = False

    #-------FUNCTIONS--------#

    #FUNCTION TO PLAY SELECTED SONG
    def play_selected(self,event):
        #first create a var for selected song
        selected_song = self.Listbox.get(self.Listbox.curselection())
        self.current_song = selected_song
        #from the selected song var, put it in the curr song var
        pygame.mixer.music.load(self.current_song)
        #use the already initialised pygame module to load the current song
        self.status_var.set('Now Playing: '+ os.path.basename(self.current_song)[0:40]+'...')
        #update the status_var var with a string that says now play.. and concatenate it with the song file basename that'll be fetched by the os module
        self.progress_bar['maximum'] = pygame.mixer.Sound(self.current_song).get_length()
        #the pygame module can use the mixer sound sub module to get the length of the song and update the "maximum" item in the progress bar 
        self.update_progressbar()
        #update progressbar is a function that hasn't been written yet
        pygame.mixer.music.play()
        self.play_var.set('Pause')
        #set the play_var to pause after the pygame has completed the play() function

    #FUNCTION TO PLAY/PAUSE CURR SONG
    def play_pause(self):
        #dual functionality because the function is for one button , the pause/play button
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.play_var.set('Pause')
        #if the button is clicked it'll check the self.paused var if it is true, it'll unpause
        #and change the var (boolean) to false and set the play_var to pause
        else:
            pygame.mixer.music.pause()
            self.play_var.set('Play')
            self.paused = True
        #else, do the opposite

    #FUNCTION FOR SKIPPING 
    #BACKWARD
    def skip_backward(self):
        selection = self.Listbox.curselection()
        #create a selection var for the cur songs selected, "curselection" is a tkinter listbox function and it returns a tuple, in our case a list of songs
        if selection:
            prev_song_index = int(selection[0]) - 1
        #to get the index of the prev song convert the index of the current song in selection list to an integer and subtract by 1 to get prev songs index
            if prev_song_index >= 0 : #if the index of the prev song is greater than 0 then proceed  to play
                prev_song = self.istbox.get(prev_song_index)
                #a var for the prev song using the index we just got
                self.current_song = prev_song
                #now load the song with pygame
                pygame.mixer.music.load(self.current_song)
                self.status_var.set('Now Playing: ' + os.path.basename(self.current_song)[0:40]+'...')
                #update the status bar with the prev song name gotten by the os module    /\ this shows only the first 40 characters
                pygame.mixer.music.play(fade_ms=100)
                self.play_var.set('Pause')
                #will change the play var when the song is done
            else: #if the index is less than zero, error. if equal to 0 that's the first song
                messagebox.showwarning('warning',"this is the first song")
        else: #if theres nothing in selection
            messagebox.showerror('Error',"NO song is selected")
        
    #FORWARD
    def skip_forward(self):
        selection = self.Listbox.curselection()
        if selection:
            next_song_index = int(selection[0]) + 1
            if next_song_index < self.Listbox.size() :
            #if the next song is less than the size of the total playlist then continue "size()" is a function for getting list size
                next_song = self.Listbox.get(next_song_index)
                self.current_song = next_song
                pygame.mixer.music.load(self.current_song)
                self.status_var.set('Now Playing: '+ os.path.basename(self.current_song)[0:40]+'...')
                pygame.mixer.music.play()
                self.play_var.set('pause')

            else: #if next song index is is greater than list size. then thats the last song
                messagebox.showwarning('warning', "This is the last song")

    #FUNCTIIONS FOR VOLUME
    #volume seems in built in pygame
    def volume_set(self,val):
        volume = float(val)
        pygame.mixer.music.set_volume(volume)

    #IMPORTING THE MUSIC
    #import button
    def import_music(self):
        #import from local dir
        file_paths = filedialog.askopenfilenames()
        #file paths will be a tuple filled with filenames of the songs ig\\ filediaolog should open the windows file dialog widget for picking files from a dir

        for file_path in file_paths: #for every file path in the tuple execute the next line
            #if alread in playlist listbox dont add it again
            if file_path not in self.Listbox.get(0,tk.END):
                self.Listbox.insert(tk.END,file_path)

    def update_progressbar(self):
        #the function we put in the first play_selected function
        current_time = pygame.mixer.music.get_pos() / 1000
        #theres a pygame func that can get the time of the loaded song
        self.progress_bar['value'] = current_time
        #seems the progressbar object has components treated like a list , the "value" is the index for the value component
        minutes, seconds = divmod(int(current_time), 60)   
        #dooes floor division for int of current time and 60
        self.elapsed_time.config(text="{:02d}:{:02d}".format(minutes,seconds))
        #seems to be updating the elasped time\
        self.root.after(1000,self.update_progressbar)  
        #calls the func after 1000 ms

#Starts the app 
#give the root var the tk window val (i guess we're instantiating it)

root = tk.Tk()

#now were creating a music player object by calling the class and passing the root into it 
MusicPlayer(root)

root.mainloop()
       
            
