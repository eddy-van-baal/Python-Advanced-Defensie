#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyodbc
import psycopg2
import sys

connection_arguments = {
    'host': '172.17.0.2',      # or 'localhost'
    'port': '5432',             # default '5432'
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres'
}

conn = None
try:
    # connection_arguments = {
    #     'host': '172.17.0.2',  # or 'localhost'
    #     'port': '5432',  # default '5432'
    #     'dbname': 'postgres',
    #     'user': 'postgres',
    #     'password': 'postgres'
    # }
    # conn = psycopg2.connect(**connection_arguments)

    connection_string = "host='localhost' " \
                        "port='5432' " \
                        "dbname='postgres' " \
                        "user='postgres' " \
                        "password='postgres'"
    conn = psycopg2.connect(connection_string)

    # connection_string = "DRIVER={PostgreSQL Unicode};" \
    #                     "SERVER=172.17.0.2; " \
    #                     "PORT=5432; " \
    #                     "DATABASE=postgres; " \
    #                     "UID=postgres; " \
    #                     "PWD=postgres;"
    # conn = pyodbc.connect(connection_string)

    cur = conn.cursor()

    cur.execute("CREATE DATABASE Products;")
    cur.commit()

    cur.execute("CREATE TABLE Products(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur.execute("INSERT INTO Products VALUES(1,'Milk',5)")
    conn.execute("INSERT INTO Products VALUES(2,'Sugar',7)")
    conn.execute("INSERT INTO Products VALUES(3,'Coffee',3)")
    conn.execute("INSERT INTO Products VALUES(4,'Bread',5)")
    conn.execute("INSERT INTO Products VALUES(5,'Oranges',3)")

except psycopg2.DatabaseError as e:
    print('Error %s' % e)

    if conn:
        conn.rollback()

    sys.exit(1)

finally:
    if conn:
        conn.close()