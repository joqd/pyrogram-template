from .models import engine
from sqlalchemy.orm import Session

def make_session():
    return Session(engine)