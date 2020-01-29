from data import TAG_IDS_QUERY, USER_QUERY
from models import Post, Tag, User
from setup_db import session

if __name__ == '__main__':
    posts = session.query(Post, User, Tag).filter(Post.user_id == USER_QUERY) \
        .filter(Tag.id.in_(TAG_IDS_QUERY)).all()
    [print(p, end='\n\n') for p in posts]
