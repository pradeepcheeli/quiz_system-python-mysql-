import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@0916",
        database="quizdb"
    )
