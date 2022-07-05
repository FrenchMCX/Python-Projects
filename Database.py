import sqlite3
conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles\
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
               col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('files.db')


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg' )

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()

            cur.execute("INSERT INTO tbl_textFiles (col_fname) VALUES (?)", (x,))
            print(x)
conn.close()