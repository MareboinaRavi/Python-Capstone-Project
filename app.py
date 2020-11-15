from tkinter import *

root = Tk()
root.title("  Flames App ")
root.geometry("400x300")
root.configure()
root.resizable(width=False, height=False)
Name1 = Label(root, text="Your Name :-")
Name2 = Label(root, text="Other Name :-")
Name1.place(x=0, y=10)
Name2.place(x=0, y=40)

e1 = Entry(root, width=40)
e1.place(x=90, y=10)
e2 = Entry(root, width=40)
e2.place(x=90, y=40)

btn = Button(
    root, text="FLAMES", highlightbackground="red", fg="red", command=lambda: doFlames()
)
btn.place(x=150, y=70)


def doFlames():
    res = StringVar()
    str1 = e1.get()
    str2 = e2.get()
    name1 = str1.lower().replace(" ", "")
    name2 = str2.lower().replace(" ", "")
    for i in name1:
        for j in name2:
            if i == j:
                name1 = name1.replace(i, "", 1)
                name2 = name2.replace(i, "", 1)
                break
    count = len(name1 + name2)
    # print("count is ",count)
    if count > 0:
        listt = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
        while len(listt) > 1:
            c = count % len(listt)
            s_index = c - 1
            if s_index >= 0:
                left = listt[:s_index]
                right = listt[s_index + 1 :]
                listt = left + right
            else:
                listt = listt[: len(listt) - 1]
        # print("your both are" , listt[0] ,"According to FLAMES")
        res.set(listt[0])
    else:
        res.set(" Same ")

    win = Tk()
    win.title("Results")
    win.geometry("400x400")
    # win.configure()
    win.resizable(width=False, height=False)
    res1 = Label(win, text="You both are").place(x=0, y=10)
    e3 = Entry(win, textvariable=res, width=18).place(x=74, y=10)
    res2 = Label(win, text=" According to Flames").place(x=187, y=10)
    win.mainloop()


root.mainloop()