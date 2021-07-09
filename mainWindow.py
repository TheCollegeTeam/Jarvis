import tkinter as tk
from tkinter import Button, Frame, Image, Label, PhotoImage, font,Entry
from tkinter.constants import BOTH, BOTTOM, X, Y
from PIL import Image, ImageTk

root = tk.Tk()
# root.resizable(False,False)
root.geometry("300x520")

################################ Chat Frame ###########################
chatFrame = Frame(root,width=300,height=440,bg="gray")
chatFrame.pack(fill=BOTH,expand=1)

############################ Footer Frame ###############################
footerFrame = Frame(root,width=300,height=80,bg="green")
footerFrame.pack(side=BOTTOM,fill=X)

# Button
modeChangeButton = Button(footerFrame,text="Mode")
modeChangeButton.pack(side=tk.LEFT,padx=4,ipady=9)
# Entry
inputBox = Entry(footerFrame,font=("cursive",15),width=15)
inputBox.pack(side=tk.LEFT,padx=4,ipady=9)
#Send Button
settingImage = Image.open("resources\\images\\setting1.png")
settingImage = settingImage.resize((10,10))
img = PhotoImage(settingImage)
Label1 = Label(footerFrame,image=img)
Label1.pack()
# sendBtnImg = PhotoImage(file=settingImage)
# sendBtnImg = sendBtnImg.resize((10,10))
# sendBtn = Button(footerFrame,text="Input",image=img)
# sendBtn.pack(side=tk.LEFT,ipady=9)
root.mainloop()