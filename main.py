

import os
from sqlalchemy  import (create_engine,Integer,Column,String,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) #points current path of the file

conn = 'sqlite:///'+ os.path.join(BASE_DIR, 'user.db') # connects us  with the database 
from sqlalchemy.orm  import relationship,sessionmaker # function from the SQLAlchemy library used to define relationships between database tables.

engine =create_engine(conn,echo = True) #generate our sql

Base = declarative_base()

class User(Base):
    __tablename__ = 'users' #name of the table
    
    id =Column(Integer(), primary_key = True)
    username = Column(String(30),nullable = False)
    email = Column(String(30),nullable = True)
    
    post =relationship('post',backref = 'auther')  #first-argument is the name of the table (or model) that the relationship is being defined with 
    
    
    #to return string represetation of the object create from the above class
    def __repr__(self):
        return f"<User('{self.username}','{self.email}')>" 
    
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key =True)
    title  = Column(String(20),nullable =False)
    content = Column(String(240),nullable =False )
    user_id =Column(Integer(),ForeignKey("users.id"))
    
    def __repr__(self):
        return f"<Post('{self.title}','{self.content}')>"
    
    
Base.metadata.create_all(engine) #creating  the database

session = sessionmaker()(bind = engine)  
# allows us to create ,read , delete delete ,flash changes  onto our db
#The session will use this engine to communicate with the database.

    