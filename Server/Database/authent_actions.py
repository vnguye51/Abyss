from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .authent_declarations import Users
from .game_declarations import Player



authent_engine = create_engine("mysql+mysqlconnector://root:7182011@127.0.0.1/authentication")
authent_session = sessionmaker(bind=authent_engine)()


def create_new(username,password):
    user = Users(username=username,password=password)
    authent_session.add(user)
    authent_session.commit()

def login(username,password):
    user = authent_session.query(Users).filter(Users.username == username,Users.password==password)
    if user.all():
        return user[0].id
    return None