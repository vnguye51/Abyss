import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, ForeignKey, Boolean

engine = db.create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/online_test")
connection = engine.connect()
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(length=24),nullable=False,unique=True)
    password = Column(String(length=24),nullable=False)
    connected = Column(Boolean,nullable=False,default=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    name = Column(String(length=24),nullable=False,unique=True)
    user = relationship(User)

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer,primary_key=True)
    name = Column(String(length=24),nullable=False,unique=True)
    stack_size = Column(Integer,nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer,primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'),nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'),nullable=False)
    amount = Column(Integer,nullable=False)
    character = relationship(Character)
    item = relationship(Item)



Base.metadata.create_all(engine)
