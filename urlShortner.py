from tkinter import *

import pyshorteners


def shortenurl():
    s = pyshorteners.Shortener()
    url = e.get()
    res = s.tinyurl.short(url)
    shortened_Url = Label(root, text=res)
    root.clipboard_clear()
    root.clipboard_append(res)
    shortened_Url.pack()
    shortened_Url.place(relx=0.5, rely=0.7, anchor=CENTER)


root = Tk()
root.geometry("800x350")

root.configure(bg='DarkSeaGreen2')
myLabel = Label(root, text="Enter url to be shortened: ", bg="DarkSeaGreen2")
myLabel.pack()
myLabel.config(font=('Helvetica bold', 15))
myLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
e = Entry(root, width=50, borderwidth=10)
e.pack()
e.place(relx=0.5, rely=0.4, anchor=CENTER)
myButton = Button(root, text="Generate URL", pady=10, command=shortenurl, fg="white", bg="black")
myButton.pack()
myButton.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()