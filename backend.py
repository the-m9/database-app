import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()#id integer primary key auto-increments from 1 and will show how many records we have
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))#NULL because our id value will auto-increment
    conn.commit()
    conn.close()

def view():
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):#the user will select the entry from the list box, this will correspond to an id
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn= sqlite3.connect("books.db")
    cur= conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

    
connect()#calling function here, so that when its imported into frontend script it automatically runs

#if (1,'The Fellowship of the Ring','J.R.R Tolkien',1954,9780261102354) not in view():
#    insert('The Fellowship of the Ring','J.R.R Tolkien',1954,9780261102354)

#if (3, 'the dark','grim reaper', 0, 0000000000000) not in view():
#    insert('the dark','grim reaper', 0, 0000000000000)

#update(3, 'the death','grim reaper', 0, 0000000000000)

#delete(2)

#print(view())

#print(search(year=0))