import os
import sys
from sqlalchemy import Enum,Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key= True)
    username = Column(String(250),nullable=False)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250),nullable=False)
    email = Column(String(250),unique = True, nullable = False)
    post = relationship ('Post', uselist = False, back_populates = 'user')
    comment= relationship('Comment')
    follower= relationship('Follower')


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key= True)
    user_id = Column (Integer,ForeignKey('user.id'))
    user = relationship ('User', back_populates='post')
    comment = relationship ('Comment')
    media = relationship('Media')

class Comment(Base):
    __tablename__ = 'user_followers'
    id = Column(Integer, primary_key= True)
    comment_text = (String(250), nullable = False)
    post_id = Column(Integer,ForeignKey('post.id'))
    author_id = Column(Integer,ForeignKey('user.id')) 

class Media(Base):
    __tablename__ = 'media'
    type enum
    url = Column(String(250), nullable= False)
    post_id = Column (Integer,ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column (Integer,ForeignKey('user.id'))
    user_to_id = Column (Integer, ForeignKey('user.id'))
      



    def to_dict(self):
      return {}

render_er(Base, 'diagram.png')