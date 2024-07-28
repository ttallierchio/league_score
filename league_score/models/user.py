from league_score.models.base import Base
from sqlalchemy import Column, Integer, String,Enum

import enum

class UserLevel(enum.Enum):
    User = 1
    Manager = 2
    Admin = 3
    
class UserTable(Base):
    __tablename__ = 'user'
    id = Column("id",Integer,primary_key=True)
    user_name = Column("user_name",String,nullable=False)
    active = Column("active",Integer,default=True)
    password_hash = Column("password",String,nullable=False)
    password_salt = Column("password_salt",String,nullable=False)
    first_name = Column("first_name",String,nullable=False)
    last_name = Column("last_name",String,nullable=False)
    user_level = Column("user_level",Integer,default=1,server_default="1")
