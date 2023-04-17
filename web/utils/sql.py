'''
SQL use utilities
Author: Lai
Create Date: 2023.4.16
'''
import mysql.connector
import webconfig as config
from utils.general import *

def create_session_cursor():
    ''' Create a sql session based on the webconfig.py 
        Return the (session, cursor) directly.
    '''
    cnx = mysql.connector.connect(
            host = config.SQLConfig.host,
            port = config.SQLConfig.port,
            user = config.SQLConfig.user,
            password = config.SQLConfig.password,
            database = config.SQLConfig.database,
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
        log_catch_error(e)
        print('ERROR in executing command!')
        return False

