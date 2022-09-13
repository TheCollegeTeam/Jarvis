import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import googlesearch
import webbrowser

conn = sqlite3.connect("main.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS question_answer
(question VARCHAR(30),
answer VARCHAR(255)) """)


"""
In this file there wil be two fields first field contains question 
and second field contains corresponding answer of the questions.
The goal is to insert values by only adminstrator and it can updated 
by user using command line using update function.
"""

def get_path(query):
    # query = 'chrome'
    print("reached in get path")
    flag = False
    cur.execute("SELECT * FROM question_answer WHERE question = ?",(query,))
    result = cur.fetchone()
    if result == None:
        return flag
    return result[1]

def open_website(query):
    """
    This function open any website this 
    function uses search function which is 
    in the google search module.
    """
    try:
        chrome_path = get_path('chrome')
        for j in googlesearch.search(query, num_results=0,lang="en"):
            if chrome_path == False:
                webbrowser.open_new_tab(j)
            else:
                webbrowser.get(chrome_path).open(j)
    except Exception as e:
        print(e)

def openApp(query):
    print("reached in open App function")
    query = query.replace("open","")
    query = query.replace(" ","")
    path = get_path(query)
    if path==False:
        open_website(query)
    else:
        os.startfile(path)

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",END,values=i)

def search():
    q2 = q.get()
    cur.execute("""SELECT * FROM question_answer WHERE question = ? """,(q2,))
    rows = cur.fetchall()
    update(rows)

def clear():
    cur.execute("SELECT * FROM question_answer")
    rows = cur.fetchall()
    update(rows)

def get_row(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'][0])
    t2.set(item['values'][1])

def update_data():
    application_name = t1.get()
    application_path = t2.get()
    cur.execute("UPDATE question_answer SET answer = ? WHERE question = ?",(application_path,application_name))
    entlbl1.delete(0,END)
    entlbl2.delete(0,END)
    conn.commit()
    clear()

def add_data():
    application_name = t1.get()
    application_path = t2.get()
    cur.execute("INSERT INTO question_answer(question, answer)VALUES(?,?)",(application_name,application_path))
    entlbl1.delete(0,END)
    entlbl2.delete(0,END)
    conn.commit()
    clear()

def delete_data():
    question = t1.get()
    if messagebox.askyesno("Are You sure :"):
        cur.execute("DELETE FROM question_answer WHERE question=?",(question,))
        entlbl1.delete(0,END)
        entlbl2.delete(0,END)
        conn.commit()
        clear()
    else:
        pass

def setting_page():
    root = Tk()
    root.config(bg="black")
    root.attributes("-alpha",0.9)
    global trv, q, t1, t2, entlbl1,entlbl2
    q = StringVar() 
    t1 = StringVar() 
    t2 = StringVar() 
    #========================== Createing Frame ===============================
    wrapper1 = LabelFrame(root,text="Application List",font=("none",20,"bold"),bg="#80d199")
    wrapper2 = LabelFrame(root,text="Search",font=("none",20,"bold"),bg="#80d199")
    wrapper3 = LabelFrame(root,text="Application Data",font=("none",20,"bold"),bg="#80d199")

    #=========================== Packing Frame ================================
    wrapper1.pack(fill='both',expand="yes",padx=20,pady=10)
    wrapper2.pack(fill='both',expand="yes",padx=20,pady=10)
    wrapper3.pack(fill='both',expand="yes",padx=20,pady=10)

    ##########################################################################
    #                               Label                                    #
    #                               Frame1                                   #
    ##########################################################################
    #=========================== Creating Tree View ===========================
    trv = ttk.Treeview(wrapper1,columns=(1,2),show="headings",height="6")
    trv.pack(fill=BOTH,expand=1)
    #============================= Creating Heading ===========================
    trv.heading(1,text="Application Name")
    trv.heading(2,text="Application Path")

    cur.execute("SELECT * FROM question_answer")
    rows = cur.fetchall()
    #================================ Calling Update Function =================
    update(rows)

    ##########################################################################
    #                               Label                                    #
    #                               Frame2                                   #
    ##########################################################################

    #================================= Search section ===========================

    #============================== Search Label ================================
    lbl = Label(wrapper2,text="Search",font=("cursive",13),fg="black",bg="#80d199")
    lbl.pack(side=tk.LEFT,padx=10)

    ent = Entry(wrapper2,textvariable=q,font=(13))
    ent.pack(side=tk.LEFT,padx=6)

    #========================== Search Button ===================================
    btn = Button(wrapper2,text="Search",command= search,width=20,bg="black",fg="white")
    btn.pack(side=tk.LEFT,padx=6)

    #============================ Clear Button ==================================
    clearbtn = Button(wrapper2,text="clear",command=clear,width=20,bg="black",fg="white")
    clearbtn.pack(side=tk.LEFT,padx=6)

    ##########################################################################
    #                               Label                                    #
    #                               Frame3                                   #
    ##########################################################################

    #============================ Application Name ================================
    lbl1 = Label(wrapper3,text="Application Name",font=("cursive",13),fg="black",bg="#80d199")
    lbl1.grid(row=0,column=0,padx=5,pady=3)

    entlbl1 = Entry(wrapper3,textvariable=t1,font=(13))
    entlbl1.grid(row=0,column=1,padx=5,pady=3)

    #============================= Application path ===============================
    lbl2 = Label(wrapper3,text="Application Path",font=("cursive",13),fg="black",bg="#80d199")
    lbl2.grid(row=1,column=0,padx=5,pady=3)

    entlbl2 = Entry(wrapper3,textvariable=t2,font=(13))
    entlbl2.grid(row=1,column=1,padx=5,pady=3)

    #============================= Update Button ===================================
    updateBtn = Button(wrapper3,text="Update",command=update_data,bg="black",fg='white',width=20)
    updateBtn.grid(row=4,column=1,padx=5,pady=7)

    #================================= Delete Button ===============================
    deleteBtn = Button(wrapper3,text="Delete",command=delete_data,bg="black",fg='white',width=20)
    deleteBtn.grid(row=4,column=2,padx=5,pady=7)

    #=================================== Add Button ================================
    addBtn = Button(wrapper3,text="Add",command=add_data,bg="black",fg='white',width=20)
    addBtn.grid(row=4,column=0,padx=5,pady=7)

    #==================================Event ========================================
    trv.bind('<Double 1>',get_row)

    root.title("Tree view")
    root.geometry("700x600")
    root.resizable(False,False)

    root.mainloop()

if __name__=="__main__":
    # =======================Calling Setting page================================
    print("humra setting")
    setting_page()
    # query = input("Enter Query :")
    # openApp(query)
    # conn.close()