__author__ = 'J Tas'

import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',database='python_mysql', user='root', password='secret')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


def main():
    connect()

if __name__ == "__main__":
    main()
