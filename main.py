

import os
from sqlalchemy  import create_engine
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn = 'sqlite:///'+ os.path.join(BASE_DIR, 'user.db')

engine =create_engine(conn,echo = True)

Base = declarative_base

