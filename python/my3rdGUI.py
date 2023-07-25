from tkinter import *
root = Tk()
root.title("open file")
root.geometry("500x450")
def open_txt():
    text_file = open("testgui.txt", 'r')
    contents = text_file.read()
    my_text.insert(END,contents)
    text_file.close()
my_text = Text(root, width = 40, height=10, font=("Helvetica",.16))
my_text.Pack(pady=20)
open_button = Button(root, text="open text file", command=open_txt)
open_button.Pack(pady=20)
root.mainloop()
