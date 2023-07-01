from .models import *
from pony.orm import db_session

from datetime import datetime
from uuid import uuid4


@db_session
def get_user(user_id):
    return User.get(id=str(user_id))

@db_session
def add_user(user_id, name='Unknow'):
    return User(id=str(user_id), name=name, timestamp=datetime.now())
