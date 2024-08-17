#import sqlite3 for database storage
#===================================
import sqlite3
import time as tim
##
###create connection to sqlite3
###====================================
##conn = sqlite3.connect('datafile.db')
##
###create cursor for dbconnection
###====================================
##cursor = conn.cursor()
##
##
###Create a table in the database to query later
###====================================
##cursor.execute('DROP TABLE IF EXISTS people;')
##
##cursor.execute(
##'''
##CREATE TABLE people
##(
##    id INTEGER PRIMARY KEY
##    ,name varchar(50) NOT NULL
##    ,count INTEGER
##)
##'''
##)
##
##cursor.execute(
##'''
##    INSERT INTO people (name, count) VALUES ("Jill", 15)
##'''
##              )
##
##cursor.execute(
##'''
##    INSERT INTO people (name, count) VALUES ("Bob", 20)
##'''
##              )
##cursor.execute(
##'''
##    INSERT INTO people (name, count) VALUES ("Sue", 10)
##'''
##              )

#Query the database table and sotre result as variable
#====================================
#result = cursor.execute('''SELECT * FROM people''')

#Query the database table and sotre result as variable
#====================================
#result2 = cursor.execute('''SELECT * FROM people Where name = "Jill"''')

#iterate over results with for loop
#====================================
#result3 = cursor.execute(''' SELECT * FROM people''')
#for row in result3:
#    print(row)


# Commit changes made to database, before closing it
#======================================
##conn.commit()

#conn.close()
#tim.sleep(2)

#//////////////////////////////////////////////////
#===================================================
# Repeat the same steps , but do it in sqlalchemy (ORM -  Object relational mapping)
# Apparently its better than sqllite, as has beeter integration with SQL and python
#====================================================
######import sqlalchemy as sa
######from sqlalchemy.orm import sessionmaker
######
####### Set up connection and create people table
#######-----------------------------------------------------
######dbpath      = 'datafile.db'
######engine      =  sa.create_engine(url = 'sqlite:///%s' %dbpath)
######metadata    = sa.MetaData(engine)
######people      = sa.Table('people'
######                        ,metadata
######                       ,sa.Column('id',sa.Integer,primary_key = True)
######                       ,sa.Column('name', sa.String(100))
######                       ,sa.Column('count', sa.INT)
######                       )
######
####### Create session with metadata?
#######-----------------------------------------------------
######Session = sessionmaker(bind = engine)                               # Using sqlite engine creation
######session = Session()                                                 # Instantiate session
######metadata.create_all(bind = engine)                                  # Create tables stored in metadata (people table), using sqllite3 engine
######
####### One way to insert values into the table created previously (there are many ways)
#######--------------------------------------------------------
######people_ins = people.insert().values(name = 'Louis', count = '30')   # Inserts record into people table
######str(people_ins)                                                     # Outputs the SQL query behind the line above
######session.execute(people_ins)                                         # Executes the SQL query
######session.commit()                                                    # Commit Current transaction to implement changes
######
######
####### See result from people table, after insert has been conducted
#######-------------------------------------------------------
######result4 = session.execute(sa.select([people]))                       # Stores results of select statment into results4
######
######for row in result4:
######    print(row)


#//////////////////////////////////////////////////////////////////
#__________________________________________________________________
#//////////////////////////////////////////////////////////////////
# Now to use a libary called alembic, as a lightwiegh database migration tool
#==================================================================





#//////////////////////////////////////////////////////////////////
#__________________________________________________________________
#//////////////////////////////////////////////////////////////////
# Now , onto using NoSQL !! firstly using Redis ( stands for Remote Dctionary Server_ - think key-values pair vibe)
#==================================================================
# import relevant libraries
#------------------------------------------------------------------
import redis as red

#inititate a local redis server
#------------------------------------------------------------------
r = red.Redis(host = 'localhost',port = 6379)

#get list of keys from the database
#------------------------------------------------------------------
##r.set(name = 'a_key',value = 'a_value')
##True
##r.keys()
##[b'a_key']
##v = r.get('a_key')
##v
##b'a_value'
##r.incr('counter')
##1
##r.get('counter')
##b'1'
##r.incr('counter')
##2
##r.get('counter')
##b'2'
##r.push("words","two")
##Traceback (most recent call last):
##  File "<pyshell#12>", line 1, in <module>
##    r.push("words","two")
##
##r.rpush("words","two")
##1
##r.lrange("words",0,-1)
##[b'two']
##r.rpush("words","Three")
##2
##r.lrange("words",0,-1)
##[b'two', b'Three']
##rllen("words")
##Traceback (most recent call last):
##  File "<pyshell#17>", line 1, in <module>
##    rllen("words")
##NameError: name 'rllen' is not defined
##r.llen("words")
##2
##r.lpush("words","zero")
##3
##r.lrange("words",0, -1)
##[b'zero', b'two', b'Three']
##r.lindex("words",1)
##b'two'

#//////////////////////////////////////////////////////////////////
#__________________________________________________________________
#//////////////////////////////////////////////////////////////////
# Another NoSQL !! using MongoDB
#==================================================================

from pymongo import MongoClient

mongo = MongoClient(host = 'localhost', port = 27017)


import datetime
a_document = {'name': 'Jane',
'age': 34,
'interests': ['Python', 'databases', 'statistics'],
'date_added': [datetime.datetime.now()]
}

db = mongo.my_data
collection = db.docs
collection.find_one()
db.collection_names()
[]
