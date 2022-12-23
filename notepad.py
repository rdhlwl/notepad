from tkinter import *
from tkinter.filedialog import *
import ctypes
import sys

#window
window = Tk()

window.title("Notepad")

window.geometry("400x600")
window.config(bg = "#212121")

ctypes.windll.shcore.SetProcessDpiAwareness(1) #quality


#textbox
text_box = Text(window, wrap = "word", width = 100,bg = "#212121",insertbackground='white',
        fg="white", font = ("Cascadia Mono", 16))
text_box.pack(padx = 10, pady = 10, expand=True, fill="both")


#retrieves input from text_box and checks for commands 
def getInput(enterpress):
    input = text_box.get(1.0, "end-1c")
    inputlist = input.split()
    for el in inputlist:
        if el == "!open":
            openFile()
        elif el == "!save":
            saveFile()
        elif el == "!clear":
            clearContents()
        elif el == "!close":
            closeFile()
        else:
            continue


#prompts user to open a file
def openFile():
    path = askopenfilename(title = "Select a File",
        filetypes= (("Text Files", "*.txt"),))
    f = open(path, encoding="utf8")
    filepath = path
    if f is not None:
        content = f.read()
    f.close()
    text_box.delete(1.0, "end")
    text_box.insert(1.0, content)
    return filepath
        

#saves file and exits
def saveFile():
    new_file = asksaveasfile(initialfile = 'Untitled.txt', filetypes=[("Text Documents","*.txt")])
    if new_file is None:
        pass
    write_text = str(text_box.get(1.0, "end-7c")) #deletes the command
    new_file.write(write_text)
    new_file.close()
    sys.exit()


#clears file contents
def clearContents():
    text_box.delete(1.0,"end")


#closes the file
def closeFile():
    sys.exit()


window.bind("<Return>", getInput)

#run
window.mainloop()