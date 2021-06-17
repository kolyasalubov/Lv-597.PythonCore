# This tasks reminder provides a user with a notification of tasks to be performed and
# was created as part of the Python Core course delivered by a digital consulting company SoftServe

import tkinter 
import threading
import sys
from tkinter import messagebox

tasks = []
real_timer = threading
timer = threading
r_thread = True

#application functions

def get_entry(event=""):
    text = taskrem.get()
    hour = int(time.get())
    taskrem.delete(0, tkinter.END)
    time.delete(0, tkinter.END)
    taskrem.focus_set()
    add_list(text, hour)
    


def add_list(text, hour):
    tasks.append([text, hour])
    timer = threading.Timer(hour, time_passed, [text])
    timer.start() 


def update_list():
    if taskremlist.size() > 0:
        taskremlist.delete(0, "end")
    for task in tasks:
        taskremlist.insert("end", "[" + task[0] + "] Time left: " + str(task[1]) + "in secondes")


def time_passed(task):
    tkinter.messagebox.showinfo("Please be reminded", "It is time for : " + task)


def real_time():
    if r_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task in tasks:
        if task[1] == 0:
            tasks.remove(task)
        task[1] -= 1
    update_list()


if __name__ == '__main__':

    # application 
    app = tkinter.Tk()
    app.geometry("520x720")
    app.title("Tasks reminder") 
    app.rowconfigure(0, weight=1)

    # fen
    frame = tkinter.Frame(app)
    frame.pack()

    # widgets
    label = tkinter.Label(app, text="Enter task/s to be undertaken",
                          wraplength = 200,
                          justify = tkinter.LEFT)
    label_hour = tkinter.Label(app, text="Enter time left (in secondes)",
                               wraplength = 200,
                               justify = tkinter.LEFT)
    taskrem = tkinter.Entry(app, width=35)
    time = tkinter.Entry(app, width=20)
    send = tkinter.Button(app, text='Add', fg="#ffffff", bg='#6186AC', height=2, width=25, command=get_entry)
    quit = tkinter.Button(app, text='Exit', fg="#ffffff", bg='#EB6464', height=3, width=30, command=app.destroy)
    taskremlist = tkinter.Listbox(app)
    if tasks != "":
        real_time()

    # binding
    app.bind('<Return>', get_entry)
    
    # widgets 
    label.place(x=0, y=10, width=190, height=23)
    label_hour.place(x=225, y=10, width=190, height=23)
    taskrem.place(x=60, y=30, width=190, height=23)
    time.place(x=265, y=30, width=48, height=23)
    send.place(x=60, y=60, width=48, height=23)
    quit.place(x=300, y=60, width=28, height=23)
    taskremlist.place(x=60, y = 100, width=280, height=280)

    app.mainloop()
    r_thread = False
    sys.exit("Finished")