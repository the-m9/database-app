""" 
This is a program that stores book information:
Title, Author, Year, ISBN

User can:
search entry
add entry
update entry 
delete 
close

It is often useful to draw a sketch of your GUI before designing it
"""#sidenote, you can use multiline strings as comments or to format the output how it looks

import tkinter as t
import backend #this brings in out database file so we can access its functions

def get_selected_row(event):#event is a special parameter, which holds the information about the widget event
    try:
        global selected_tuple #this turns selected_tuple into a global variable, which can be used anywhere in the script. when the variable is used, the function is auto called    
        index=list1.curselection()[0]#this returns the position of the object in the listbox. we have [0] because the index is returned as a tuple of form (index,)
        selected_tuple = list1.get(index)
        e1.delete(0,t.END)              #the below just puts in the values into the entryboxes
        e1.insert(t.END,selected_tuple[1])
        e2.delete(0,t.END)
        e2.insert(t.END,selected_tuple[2])
        e3.delete(0,t.END)
        e3.insert(t.END,selected_tuple[3])
        e4.delete(0,t.END)
        e4.insert(t.END,selected_tuple[4])
    except:
        pass#means do nothing
    
#we cannot just call this function, because we don't input the event parameter 

def view_command():
    list1.delete(0,t.END)#this will empty the listbox before opening it
    for row in backend.view():
        list1.insert(t.END,row)#this will insert each row at the end of the list box, so its numbered properly 

def search_command():
    list1.delete(0,t.END)#our search results will be inserted into the list box
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(t.END,row)

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,t.END)
    for row in backend.view():
        list1.insert(t.END,row)#puts the updated database contents in listbox    

def delete_command():
    backend.delete(selected_tuple[0])#this deletes the row using the id of the selected row
    list1.delete(0,t.END)
    for row in backend.view():
        list1.insert(t.END,row)#puts the updated database contents in listbox

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,t.END)
    for row in backend.view():
        list1.insert(t.END,row)#puts the updated database contents in listbox





window = t.Tk()

window.wm_title('Bookbase')

window.iconbitmap(r'C:\Programming\Python_course\databaseapp\bookbase\book.ico')#this changes the window icon

title = t.Label(window,text='Title') #creating the label widgets
title.grid(row=0,column=0)

author = t.Label(window, text='Author')
author.grid(row=0,column=2)

year = t.Label(window, text='Year')
year.grid(row=1,column=0)

isbn = t.Label(window, text='ISBN')
isbn.grid(row=1,column=2)

title_text= t.StringVar() #creating the entry widgets, stringvar is the function which takes the user entry
e1= t.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text= t.StringVar() 
e2= t.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text= t.StringVar() 
e3= t.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text= t.StringVar() 
e4= t.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#creating the listbox which will display our entries
list1= t.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)#rowspan and columnspan show how many rows and columns the listbox takes up

#creating the scrollbar which will scroll our list in the y-direction
sb1= t.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)#this sets the scrollbar to scroll the y direction of the list
sb1.configure(command=list1.yview)#this tells the scrollbar that scrolling it will cause change as above

sb2= t.Scrollbar(window, orient='horizontal')
sb2.grid(row=8, column=0, columnspan=2)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)#this allows selection of rows inside the listbox. first param is event type, second is command

b1= t.Button(window, text='View all',width=12,command=view_command)#there are no brackets so the function is called when button is clicked. This is called a wrapper function
b1.grid(row=2, column=3)

b2= t.Button(window, text='Search entry', width=12,command=search_command)
b2.grid(row=3, column=3)

b3= t.Button(window, text='Add entry',width=12,command=insert_command)
b3.grid(row=4, column=3)

b4= t.Button(window, text='Update',width=12,command=update_command)
b4.grid(row=5, column=3)

b5= t.Button(window, text='Delete',width=12,command=delete_command)
b5.grid(row=6, column=3)

b6= t.Button(window, text='Close', width=12,command=window.destroy)#this attribute just closes the window
b6.grid(row=7, column=3)

view_command()#this will show all the entries in the list box upon opening

window.mainloop()