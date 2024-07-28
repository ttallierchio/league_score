from sqlalchemy import create_engine


class DataAccess():
    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///league_data.db", echo=True)
        
    def connect(self):
        conn = self.engine.connect()
        return conn
        
