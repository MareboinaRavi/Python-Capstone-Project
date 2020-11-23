"""
	 Python Script for Search Direct from Wikipedia (GUI)
	 @Mareboina_Ravi
"""
#importing libraries
import wikipedia
import tkinter
from tkinter.messagebox import showinfo

#Creatin window obj
win = Tk()
win.title("Wikipedia")
win.geometry('200*70')


#function
def search_wiki():
	search = entry.get()
	ans = wikipedia.summary(search)
	showinfo("Wikipedia Answer : ",ans)
#Creating label
label = Label(win,text="Wikipedia Search")
label.grid(row=0,column=0)

#Creating Entry Box
entry = Entry(win)
entry.grid(row=1, column=0)

#creating Button
btn = Button(win,text="Search",command=search_wiki)
btn.grid(row=1,column=1,padx=10)

win.mainloop()