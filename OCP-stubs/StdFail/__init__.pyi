import OCP.StdFail
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
__all__  = [
"StdFail_InfiniteSolutions",
"StdFail_NotDone",
"StdFail_Undefined",
"StdFail_UndefinedDerivative",
"StdFail_UndefinedValue"
]
class StdFail_InfiniteSolutions(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.StdFail', '__weakref__': <attribute '__weakref__' of 'StdFail_InfiniteSolutions' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'StdFail_InfiniteSolutions' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class StdFail_NotDone(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.StdFail', '__weakref__': <attribute '__weakref__' of 'StdFail_NotDone' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'StdFail_NotDone' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class StdFail_Undefined(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.StdFail', '__weakref__': <attribute '__weakref__' of 'StdFail_Undefined' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'StdFail_Undefined' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class StdFail_UndefinedDerivative(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.StdFail', '__weakref__': <attribute '__weakref__' of 'StdFail_UndefinedDerivative' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'StdFail_UndefinedDerivative' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class StdFail_UndefinedValue(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.StdFail', '__weakref__': <attribute '__weakref__' of 'StdFail_UndefinedValue' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'StdFail_UndefinedValue' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
