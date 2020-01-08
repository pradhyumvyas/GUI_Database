from tkinter import *
import sqlite3


root = Tk()
root.geometry("400x400")
root.title("Pradhyum")

if  __name__ == "__main__":
    #Database crated
    con = sqlite3.connect('Database.db')


    #Datbase connection

    cur = con.cursor()

    #Table Creation
    cur.execute(""" CREATE TABLE address_book(
    
        FIRST_NAME text,
        LAST_NAME text,
        ADDRESS text,
        CITY text,
        STATE text,
        ZIPCODE integer
    )
    """)

    #Commit changes

    con.commit()


    #Close connection
    con.close()



#mainloop
root.mainloop()