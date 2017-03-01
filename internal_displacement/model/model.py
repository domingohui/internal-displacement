from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
Session = sessionmaker()

class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    @classmethod
    def lookup(cls, session, description):
        return session.query(cls).filter_by(description=description).one()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    @classmethod
    def lookup(cls, session, description):
        return session.query(cls).filter_by(description=description).one()


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    domain = Column(String)
    status_id = Column('status', Integer, ForeignKey('status.id'))
    status = relationship('Status')
