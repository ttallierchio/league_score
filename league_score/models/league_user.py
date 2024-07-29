from league_score.models.base import Base
from sqlalchemy import Column, Integer

class LeagueUserTable(Base):
    __tablename__ = 'league_user'
    id = Column("id",Integer,primary_key=True)
    league_id = Column("league_id",Integer,primary_key=True)
    player_id = Column("player_id",Integer,primary_key=True)