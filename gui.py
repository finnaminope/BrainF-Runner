from tkinter import *
from tkinter import filedialog
import runBf
import os

def StartGui():
  #Define the tkinter instance
  win= Toplevel()
  win.title("Rounded Button")

  #Define the size of the tkinter frame

  #Import the image using PhotoImage function
  click_btn= PhotoImage(file='play.png')

  #Let us create a label for button event
  img_label= Label(image=click_btn)
  def select_file(ft):
    filename = filedialog.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=ft)
    return filename

  #Let us create a dummy button and pass the image
  button= Button(win, text="run a bfa program",command= lambda: runBf.BulidProgFunctions.RunFile(select_file((
        ('BrainF Advanced Files', '*.bfa'),
        ('BrainF Files', '*.bf'),
        ('All Files', '*.*')
    )), select_file((
        ('Compiled Bfa Syntax Files', '*.CBFASSF'),
    ))),
  borderwidth=0)
  button.pack(pady=30)

  win.mainloop()
