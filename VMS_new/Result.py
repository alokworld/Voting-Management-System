import sqlite3
from CentralBody.Passkey import Passkey

vote_instance=Passkey()

conn = sqlite3.connect('test.db')
def result():
    s=""
    while s!=vote_instance._Passkey__pass:
        print("For Accessing The Result Enter Passkey:")
        s=input()

    print("----------------------- Results -----------------------")
    cursor=conn.execute(''' select * from Election''')
    for row in cursor:
        print(row)
    print("-------------------------------------------------------")
    result = conn.execute('''
    SELECT id, Name
    FROM Election
    ORDER BY count DESC
    LIMIT 1;
    ''')
    row = result.fetchone()
    highest_count_id = row[0]
    highest_count_name = row[1]
    print("The Winner Is:")
    print(f"ID: {highest_count_id}, Name: {highest_count_name}")
    conn.close()

result()