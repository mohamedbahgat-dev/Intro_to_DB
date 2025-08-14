import mysql.connector

try:
    mydb = mysql.connector.connect(
     host="localhost",
    user="root",
    password="Tayseermuhamed123@",
    database="alx_book_store"
   )
    
    mycursor = mydb.cursor()

    mycursor.execute("""
    CREATE DATABASE IF NOT EXISTS alx_book_store
    """)

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Connection Error: {err.msg}")

finally:
    mycursor.close()
    mydb.close()
    print('Database connection closed.')
    




