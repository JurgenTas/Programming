__author__ = 'J Tas'

from mysql.connector import MySQLConnection, Error

db_config = {
    'user': 'jurgen',
    'password': 'test',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True,
}


def query(sql_command):
    """ Connect to MySQL database """
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(sql_command)
        conn.commit()  # accept the changes

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print('Connection closed.')


def main():
    sql_command = """
    CREATE TABLE employee (
    staff_number INTEGER PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(30),
    gender CHAR(1),
    joining DATE,
    birth_date DATE);"""
    query(sql_command)

    staff_data = [("1", "William", "Shakespeare", "m", "1961-10-25"), ("2", "Frank", "Schiller", "m", "1955-08-17"),
                  ("3", "Jane", "Wall", "f", "1989-03-14")]

    for p in staff_data:
        format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
        VALUES ({number}, "{first}", "{last}", "{gender}", "{birthdate}");"""
        sql_command = format_str.format(number=p[0], first=p[1], last=p[2], gender=p[3], birthdate=p[4])
        query(sql_command)

if __name__ == "__main__":
    main()

