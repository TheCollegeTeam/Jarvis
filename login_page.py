import tkinter as tk
from tkinter import Button, Frame, Label, StringVar, ttk
from tkinter import font
from tkinter.constants import BOTH, CENTER
from  PIL import Image, ImageTk
import os

def auto_login():
    f = open ("userDetails\\userdetail.txt","r")
    data = f.readline()
    data = data.split(":")
    # print(f"your name is {data[0]} and you are {data[1]}")
    return data
#------------------------------------ Add user ------------------------------------------
def add_user():
    """
    When user click on add user button then this 
    function will execute. This function get values 
    from entry box and checks if all details
    are filled or not if not if will show 
    error on screen if all details are filled then 
    it will write details on userdetails.txt 
    """
    username = userName.get()
    gender = selected.get()
    lblFrame =Frame(root,width=380,height=100)
    lblFrame.place(x=0,y=470)
    if username == "" or gender == "":
        if username =="" and gender != "":
            noUserName = Label(root,text="(Please Enter user name)",fg="red")
            noUserName.place(x=120,y=480)
            # print("Please Enter user name")
        elif username !="" and gender == "":
            # print("Please Select gender ")
            noGender = Label(root,text="(choose your Gender)",fg="red")
            noGender.place(x=120,y=480)
        else:
            # print("Please Enter user Details")
            noDetail =  Label(root,text="(Enter Your Details first)",fg="red")
            noDetail.place(x=120,y=480)
    else: 
        callMe = "sir"
        if gender == "female":
            callMe = "ma'am"
        pathUserDetail = "userDetails"
        if os.path.isdir(pathUserDetail):
            file_path = f"userDetails\\userdetail.txt"
            with open (file_path,"w") as file:
                file.write(f"{username.lower()}:{gender}")
                # print(f"{username}:{gender}")
            allDetails = Label(root,text=f"Congratulation {callMe}",font=("arial bold",15))
            allDetails.place(x=100,y=480)
            root.after(10000,lambda:root.destroy())
        else:
            os.makedirs("userDetails")
            add_user()

def create_login_window():
    """
    This Function create a login window
    where user fills details and click on 
    add user button and add button call
    a function add user.
    """
    global root,userName,selected
    root = tk.Tk()
    root.geometry("380x650+500+0")
    root.resizable(False,False)
    #----------------------------------- Variable ------------------------------------------
    userName = StringVar()
    selected = StringVar()

    #------------------------------------- creating frame -------------------------------------------
    frameWidth =380
    frameHeight = 270
    frameTop = Frame(root,width=frameWidth,height=frameHeight,bg="grey")
    frameTop.pack()
    #------------------------------------- Displaying a Image ----------------------------------------
    img = Image.open("resources\\images\\samImg.gif")
    resizeImg = img.resize((frameWidth,frameHeight))
    imgTest = ImageTk.PhotoImage(resizeImg)
    imgLbl = tk.Label(frameTop,image=imgTest)
    imgLbl.pack()
    user_name = tk.Label(root,text="Your Name",font=("Arial",13))
    user_name.place(x=40,y=300)
    user_name_entry = tk.Entry(root,font=("Arial",13),textvariable=userName)
    user_name_entry.place(x=160,y=300)


    #------------------------------------- Creating Radio Button --------------------------------------

    r1 = ttk.Radiobutton( text='Male', value="male", variable=selected)
    r1.place(x=60,y=350)
    r2 = ttk.Radiobutton( text='Female', value="female", variable=selected)
    r2.place(x=180,y=350)

    # ----------------------------- Login Button ------------------------------------------------------
    loginBtn = Button(root,text="Add User",command=add_user,bg="green",fg="white",width=40)
    loginBtn.place(x=40,y=430)

    root.mainloop()

if __name__== "__main__":
    path = "userDetails\\userdetail.txt"
    if os.path.exists(path)==False:
        create_login_window()
    else:
        pass