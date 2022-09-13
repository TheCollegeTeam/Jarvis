import tkinter as tk
def myBirthday():
    try:
        root = tk.Tk()
        image1 = tk.Image.open("resources\\images\\birthdayImg.png")
        test = tk.ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.pack()
        root.after(10000,lambda:root.destroy())
        root.mainloop()
    except Exception as e:
        print(e)