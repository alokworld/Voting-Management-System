import sqlite3

print("Do You Want Default Candidates or New?")
print("Default: 0")
print("New: 1")
i = int(input())

def c_database():
    conn = sqlite3.connect('test.db')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Election (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            count INTEGER
            )
        ''')

    if not i:
        conn.execute('''DELETE FROM Election''')
        conn.commit()
        conn.execute('''
            INSERT INTO Election (id, Name, count)
            VALUES 
                (1, "Sachin Tendulkar", 0),
                (2, "Virat Kohli", 0),
                (3, "MS Dhoni", 0);
        ''')
        conn.commit()
    else:
        print("Number of Candidates You Want, Due to GUI restrictions Enter 3")
        c = int(input())
        conn.execute('''DELETE FROM Election''')
        conn.commit()

        while c != 0:
            print("Enter ID:")
            id = int(input())
            print("Enter Name:")
            name = input()
            conn.execute('''
            INSERT INTO Election (id, Name, count)
            VALUES (?, ?, 0)
            ''', (id, name))
            conn.commit()
            c = c - 1

    conn.close()

c_database()