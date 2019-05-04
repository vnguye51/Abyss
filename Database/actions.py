from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarations import Item, Player, Inventory

engine = create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/online_test")
session = sessionmaker(bind=engine)()

class Players:
    def create_new(self,name):
        new_player = Player(name=name)
        session.add(new_player)
        session.commit()

class Inventories:
    def add_item(self,item_id,player_id):
        new_item = Inventory(item_id=item_id,player_id=player_id)
        session.add(new_item)
        session.commit()
