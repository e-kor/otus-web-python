import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from data import DB_NAME

engine = sqlalchemy.create_engine(f'sqlite:///{DB_NAME}', echo=False)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session: Session = Session()
