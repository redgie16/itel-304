from flask import g
import sqlite3

def connect_to_database():
   conn = sqlite3.connect('crudapplication.db')
   conn.row_factory = sqlite3.Row
   return conn

def get_database():
   if not hasattr(g, 'crudapplication_db'):
      g.crudapplication_db = connect_to_database()
   
   return g.crudapplication_db


