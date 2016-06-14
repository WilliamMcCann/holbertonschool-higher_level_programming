#!/usr/bin/python
import sys
import BaseModel
import School
import Batch
import User
import Student

if len(sys.argv) < 2:
    print 'Please enter an action'
if sys.argv[1] not in ['create', 'print', 'insert', 'delete']:
    print 'Undefined action "' + sys.argv[1] + '"'
if sys.argv[1] in ['create', 'print', 'insert', 'delete']:
    print sys.argv[1]

db = SqliteDatabase(self)

def create(self)
    db.create_tables(self.class)

def print(self)
    print 

def insert

def delete
