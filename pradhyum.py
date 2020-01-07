from tkinter import *
import sqlite3


root = Tk()
root.geometry("400x400")
root.title("Pradhyum")

# Button Functioning

def submit():
    #Database crated
    con = sqlite3.connect('pv.db')

    #Datbase connection
    cur = con.cursor()

    #Data Inserting

    cur.execute(""" INSERT INTO address_book
    (FIRST_NAME, LAST_NAME, ADDRESS, CITY, STATE, ZIPCODE) VALUES (:a,:b,:c,:d,:e,:f)""", 

    {
        'a':first_label.get(),
        'b':last_label.get(),
        'c':address_label.get(),
        'd':city_label.get(),
        'e':state_label.get(),
        'f':zipcode_label.get()
    }

    )

    # Delete After Inserting Record
    first_label.delete(0, END)
    last_label.delete(0, END)
    address_label.delete(0, END)
    city_label.delete(0, END)
    state_label.delete(0, END)
    zipcode_label.delete(0, END)

    #Commit changes
    con.commit()

    #Close connection
    con.close()
    
# def Query_window():
#     top = Toplevel()

def Query():

    top = Toplevel()
    #Database crated
    con = sqlite3.connect('pv.db')

    #Datbase connection
    cur = con.cursor()

    #Data Fetching
    cur.execute("SELECT * FROM address_book")
    records = cur.fetchall()
    
    record_data =''
    for record in records:
        record_data += str(record) + "\n"
    
    query_fetch = Label(top, text=record_data)
    query_fetch.grid(row=10,column=1)
    
    #Commit changes
    con.commit()

    #Close connection
    con.close()





#GUI Creation
heading = Label(root, text="Welcome to my Database page")
     
    #Functioning

blank = Label(root, text="      ")
first = Label(root, text="First Name")
last = Label(root,text="Last Name")
address = Label(root,text="Address")
city = Label(root,text="City")
state = Label(root,text="State")
zipcode = Label(root,text="Zip Code")


    #Griding

heading.grid(row=0, column=2)
blank.grid(row=1,column=0)
first.grid(row=2,column=1, padx=10,pady=6)
last.grid(row=3,column=1, padx=10,pady=6)
address.grid(row=4,column=1, padx=10,pady=6)
city.grid(row=5,column=1, padx=10,pady=6)
state.grid(row=6,column=1, padx=10,pady=6)
zipcode.grid(row=7,column=1, padx=10,pady=6)

    #Labels

first_label = Entry(root, width=30)
last_label = Entry(root, width=30)
address_label = Entry(root, width=30)
city_label = Entry(root, width=30)
state_label = Entry(root, width=30)
zipcode_label = Entry(root, width=30)

    #Label Griding
first_label.grid(row=2, column=2)
last_label.grid(row=3, column=2)
address_label.grid(row=4, column=2)
city_label.grid(row=5, column=2)
state_label.grid(row=6, column=2)
zipcode_label.grid(row=7, column=2)



    #Buttons

Submit_button = Button(root, text="Submit", command=submit)
Submit_button.grid(row=8, column=2)

Query_button = Button(root,text="Show Record", command=Query)
Query_button.grid(row=9, column=1)




# #Database crated
# con = sqlite3.connect('pv.db')


# #Datbase connection
# cur = con.cursor()


# #Commit changes
# con.commit()

# #Close connection
# con.close()


#mainloop
root.mainloop()