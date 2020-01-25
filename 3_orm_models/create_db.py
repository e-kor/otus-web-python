import os

import sqlalchemy
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from data import DB_NAME, POSTS_INFO, TAG_NAMES, USER_NAMES
from models import Base, Post, Tag, User


def clear_db(filename):
    os.remove(filename)


def create_tables(engine):
    Base.metadata.create_all(engine)


def insert_users(session: Session, *usernames):
    for i, username in enumerate(usernames):
        session.add(User(id=i, username=username))
    session.commit()


def insert_tags(session: Session, *tag_names):
    for i, tag_name in enumerate(tag_names):
        session.add(Tag(id=i, name=tag_name))
    session.commit()


def insert_posts(session: Session, *posts_info):
    for i, post_info in enumerate(posts_info):
        tag_ids = post_info.pop('tag_ids')
        p = Post(**post_info)
        for tag_id in tag_ids:
            p.tags.append(session.query(Tag).filter(Tag.id == tag_id).one())
        session.add(p)
    session.commit()


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(f'sqlite:///{DB_NAME}', echo=False)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    session: Session = Session()

    clear_db(DB_NAME)
    create_tables(engine)

    insert_users(session, *USER_NAMES)
    insert_tags(session, *TAG_NAMES)
    insert_posts(session, *POSTS_INFO)
