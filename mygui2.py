from tkinter import *
import time
import tkinter.messagebox
from csvgui import response
import pyttsx3
import threading
import speech_recognition as sr 

saved_username = ["You"]
window_size="400x400"

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.tl_bg = "black"
        self.tl_bg2 = "black"
        self.tl_fg = "black"
        self.font = "Verdana 10"
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5,bg="black")
        self.text_frame = Frame(self.master, bd=6,bg="black")
        self.text_frame.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg="black", font="Verdana 10", relief=GROOVE,
                             width=10, height=1,fg="white")
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)
        self.entry_frame = Frame(self.master, bd=1,bg="black")
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)
        self.send_button = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)
        
        
    def playResponse(self,response):
        x=pyttsx3.init()
        li = []
        if len(response) > 100:
            if response.find('--') == -1:
                b = response.split('--')
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(response)
        x.runAndWait() 
    def chatexit(self):
        exit()
    
    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "User : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        ob=response(user_input)
        pr="Bot : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.entry_field.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.playResponse, args=(ob,))
        t2.start()
        
        
root=Tk()


a = ChatInterface(root)
root.geometry(window_size)
root.title("csvgui")
root.iconbitmap('favicon.ico')
root.mainloop()
