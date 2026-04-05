from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///ibps.db")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)

class Performance(Base):
    __tablename__ = "performance"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    subject = Column(String)
    topic = Column(String)
    micro_topic = Column(String)
    result = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)