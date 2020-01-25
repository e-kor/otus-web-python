import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from data import DB_NAME, TAG_IDS_QUERY, USER_QUERY
from models import Post, Tag, User

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(f'sqlite:///{DB_NAME}', echo=False)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session: Session = Session()

    posts = session.query(Post, User, Tag).filter(Post.user_id == USER_QUERY).filter(Tag.id.in_(TAG_IDS_QUERY)).all()
    [print(p, end='\n\n') for p in posts]
