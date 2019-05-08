import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, ForeignKey

engine = db.create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/authentication")
connection = engine.connect()
Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(length=24),nullable=False,unique=True)
    password = Column(String(length=24),nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
