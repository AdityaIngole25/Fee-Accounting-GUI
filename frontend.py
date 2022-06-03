from tkinter import *
import backend


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(student.get(), fees.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(student.get(), fees.get())
    list1.delete(0, END)
    list1.insert(END, (student.get(), fees.get()))


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], student.get(), fees.get())


window = Tk()
window.title("FEE INFORMATION")

l1 = Label(window, text="Student", fg="red")
l1.grid(row=0, column=0)

l2 = Label(window, text="Fees", fg="red")
l2.grid(row=0, column=2)

student = StringVar()
e1 = Entry(window, textvariable=student, borderwidth=3)
e1.grid(row=0, column=1)

fees = StringVar()
e2 = Entry(window, textvariable=fees, borderwidth=3)
e2.grid(row=0, column=3)

list1 = Listbox(window, height=8, width=35, borderwidth=5)
list1.grid(row=1, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window, bg="red")
scroll.grid(row=1, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command, fg="red")
b1.grid(row=1, column=3)

b2 = Button(window, text="Search", width=12, command=search_command, fg="red")
b2.grid(row=2, column=3)

b3 = Button(window, text="Enter", width=12, command=add_command, fg="red")
b3.grid(row=3, column=3)

b4 = Button(window, text="Update", width=12, command=update_command, fg="red")
b4.grid(row=4, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command, fg="red")
b5.grid(row=5, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy, fg="red")
b6.grid(row=6, column=3)

window.mainloop()