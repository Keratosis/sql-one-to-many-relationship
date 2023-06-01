

import os
from sqlalchemy  import (create_engine,Integer,Column,String,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) #points current path of the file

conn = 'sqlite:///'+ os.path.join(BASE_DIR, 'user.db') # connects us  with the database 

engine =create_engine(conn,echo = True) #generate our sql

Base = declarative_base()

class User(Base):
    __tablename__ = 'users' #name of the table
    
    id =Column(Integer, primary_key = True)
    username = Column(String(30),nullable = False)
    email = Column(String(30),nullable = True)
    
    
    #to return string represetation of the objct create from the above class
    def __repr__(self):
        return f"<User('{self.username}','{self.email}')>" 
    

    