from sqlalchemy import Column, Integer, String, Date
from league_score.models.base import Base

class LeagueTable(Base):
    __tablename__ = 'league'
    id = Column("id",Integer,primary_key=True)
    league_name = Column("league_name",String,nullable=False)
    active = Column("active",Integer,default=True)
    start_date = Column("start_date",Date,nullable=False)
    end_date = Column("end_date",Date,nullable=False)
    protected = Column("protected",Integer,nullable=False,default=False)
    league_password = Column("league_password",String,default="")
