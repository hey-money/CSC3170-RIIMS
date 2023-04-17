'''
General use utilities
Author: Lai
Create Date: 2023.4.16
'''
import time


def log_string(content: str):
    ''' Log a string to console with time format. '''
    print(f'[INFO] {time.ctime()}: {content}')


def log_catch_error(content: str):
    ''' Log a string to console with time format. '''
    print(f'[ERROR] {time.ctime()}: {content}')


