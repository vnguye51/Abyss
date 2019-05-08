from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from game_declarations import Item, Player, Inventory

engine = create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/online_test")
session = sessionmaker(bind=engine)()

class Players:
    def create_new(self,id,name):
        new_player = Players(name=name)
        session.add(new_player)
        session.commit()

class Inventories:
    def add_item(self,item_id,player_id,amount):
        new_item = Inventory(item_id=item_id,player_id=player_id,amount=amount)
        session.add(new_item)
        session.commit()

    def remove_item(self,item_id,player_id):   
        item = session.query(Inventory).filter(player_id=player_id,item_id=item_id)
        item.delete()
        session.commit()