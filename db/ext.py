from .models import *
from .session_factory import make_session


def get_user(user_id):
    with make_session() as session:
        return session.query(User).filter(User.id == user_id).first()


def get_users():
    with make_session() as session:
        return session.query(User).all()


def add_user(user_id, name='Unknow'):
    with make_session() as session:
        user = User(id=user_id, name=name)
        session.add(user)
        session.commit()
        return user


