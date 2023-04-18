'''
SQL use utilities
Author: Lai
Create Date: 2023.4.16
'''
import mysql.connector

def create_session_cursor():
    ''' Create a sql session based on the webconfig.py 
        Return the (session, cursor) directly.
    '''
    cnx = mysql.connector.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'czk20011201',   # change to your password!!!
            database = 'riimages',
            buffered = True
        ) 
    cur = cnx.cursor()
    return cnx, cur


def execute_fetchone(cursor, query: str, content: tuple):
    ''' Execute the query based on cursor, and fetch ONE result. '''
    cursor.execute(query, content)
    return cursor.fetchone()    

def execute_fetchall(cursor, query: str, content: tuple):
    ''' Execute the query based on cursor, and fetch ALL result. '''
    cursor.execute(query, content)
    return cursor.fetchall()   

def execute_command(cursor, cnx, command: str, content: tuple) -> bool:
    ''' Execute the sql command. This function returns 
        True if command exeucute success, False otherwise. 
    '''
    try:
        cursor.execute(command, content)
        cnx.commit()
        return True
    except Exception as e:
        print(e)
        print('ERROR in executing command!')
        return False

