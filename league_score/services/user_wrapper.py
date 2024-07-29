from league_score.services.db_wrapper import DataAccess
from league_score.models.user import UserTable,UserLevel
from sqlalchemy import select,insert
import bcrypt
from league_score.services.exceptions import AdminUserExistsException
class UserService():
    def __init__(self):
        self.db_wrapper = DataAccess()
    def validate_user(self,user_name:str,password:str):
        try:
            user_object = self.lookup_user(user_name=user_name)[0]
        except Exception as e:
            # no user found, return None
            return None
        
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'),user_object.password_salt)
        if hashed_pw.decode('utf-8') == user_object.password:
            return user_object
        else:
            return None
    
    def lookup_user(self,id:int|None=None,user_name:str|None=None,user_level:UserLevel|None=None):
        with self.db_wrapper.connect() as conn:
            stmt = select(UserTable)
            if id:
                stmt = stmt.where(UserTable.id == id)
            if user_name:
                stmt = stmt.where(UserTable.user_name==user_name)
            if user_level:
                stmt = stmt.where(UserTable.user_level == user_level.value)
            user_objs = conn.execute(stmt).all()  
            return user_objs
        
    def generate_admin_user(self):
        admin_exists = self.lookup_user(user_level=UserLevel.Admin)
        if admin_exists:
            raise AdminUserExistsException
        self.add_user("admin","admin","admin","admin",UserLevel.Admin)
        
    def add_user(self,user_name:str,password:str,first_name:str,last_name:str,user_level:UserLevel):
            bytes = password.encode('utf-8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes,salt)
            with self.db_wrapper.connect() as conn:
                stmt = insert(UserTable).values(user_name=user_name,password_salt=salt,password=hash.decode('utf-8'),user_level=user_level.value,first_name=first_name,last_name=last_name)  
                conn.execute(stmt)      
                conn.commit()    