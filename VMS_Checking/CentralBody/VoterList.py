import sqlite3


def v_database():
    conn = sqlite3.connect('voters.db')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS VoterList (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            voted BOOLEAN
            )
        ''')
    conn.execute('''
        INSERT INTO VoterList (id, Name, voted) VALUES
        (1, 'Pawan Kumar', FALSE),
        (2, 'Amit Mishra', FALSE),
        (3, 'Abhishek Gupta', FALSE),
        (4, 'Vishwa Das', FALSE),
        (5, 'Charlie', FALSE);
        ''')
    conn.commit()
v_database()