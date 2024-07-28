class ExceptionBase(Exception):
    """Should not be seen... ever
    """
    def __init__(self,msg=None,*args,**kwargs):
        super.init(msg or self.__doc__,*args,**kwargs)


class AdminUserExistsException(ExceptionBase):
    """Admin user already exists, No Need to create"""