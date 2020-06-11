import OCP.Plugin
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.Standard
__all__  = [
"Plugin",
"Plugin_Failure"
]
class Plugin():
    """
    None
    """
    @staticmethod
    def Load_s(aGUID : OCP.Standard.Standard_GUID,theVerbose : bool=True) -> OCP.Standard.Standard_Transient: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class Plugin_Failure(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.Plugin', '__weakref__': <attribute '__weakref__' of 'Plugin_Failure' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'Plugin_Failure' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
