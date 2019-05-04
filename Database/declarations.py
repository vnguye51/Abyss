import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, ForeignKey

engine = db.create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/online_test")
connection = engine.connect()
Base = declarative_base()

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer,primary_key=True)
    name = Column(String(length=24),nullable=False,unique=True)
    
class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer,primary_key=True)
    name = Column(String(length=24),nullable=False,unique=True)
    stack_size = Column(Integer,nullable=False)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer,primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'),nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'),nullable=False)
    amount = Column(Integer,nullable=False)
    player = relationship(Player)
    item = relationship(Item)
    

Base.metadata.create_all(engine)
