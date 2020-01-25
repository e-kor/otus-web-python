import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

tags_posts_table = sqlalchemy.Table('tags_posts', Base.metadata,
                                    sqlalchemy.Column('post_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('posts.id')),
                                    sqlalchemy.Column('tag_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('tags.id')),
                                    )


class Post(Base):
    __tablename__ = 'posts'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    title = sqlalchemy.Column(sqlalchemy.String(16))
    text = sqlalchemy.Column(sqlalchemy.Text)
    is_published = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    user = relationship("User", back_populates="posts", lazy='joined')
    tags = relationship("Tag", secondary=tags_posts_table, back_populates="posts")

    def __repr__(self):
        return f"Post#{self.id} by User#{self.user_id}\n" \
            f"{self.title} (Published: {self.is_published})\n" \
            f"Tags: {','.join(map(repr, self.tags))}\n" \
            f"Text: {self.text:.50s}..."


class Tag(Base):
    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)

    posts = relationship("Post", secondary=tags_posts_table, back_populates="tags")

    def __repr__(self):
        return f"Tag#{self.id} {self.name}"


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"User#{self.id} {self.username}"
