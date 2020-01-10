import sqlite3
from tkinter import *

# Button Functioning
    
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


