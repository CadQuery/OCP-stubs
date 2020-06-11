import OCP.GccEnt
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.gp
__all__  = [
"GccEnt",
"GccEnt_Array1OfPosition",
"GccEnt_BadQualifier",
"GccEnt_Position",
"GccEnt_QualifiedCirc",
"GccEnt_QualifiedLin",
"GccEnt_enclosed",
"GccEnt_enclosing",
"GccEnt_noqualifier",
"GccEnt_outside",
"GccEnt_unqualified"
]
class GccEnt():
    """
    This package provides an implementation of the qualified entities useful to create 2d entities with geometric constraints. The qualifier explains which subfamily of solutions we want to obtain. It uses the following law: the matter/the interior side is at the left of the line, if we go from the beginning to the end. The qualifiers are: Enclosing : the solution(s) must enclose the argument. Enclosed : the solution(s) must be enclosed in the argument. Outside : both the solution(s) and the argument must be outside to each other. Unqualified : the position is undefined, so give all the solutions. The use of a qualifier is always required if such subfamilies exist. For example, it is not used for a point. Note: the interior of a curve is defined as the left-hand side of the curve in relation to its orientation.
    """
    @staticmethod
    @overload
    def Enclosed_s(Obj : OCP.gp.gp_Lin2d) -> GccEnt_QualifiedLin: 
        """
        Constructs a qualified line, so that the solution computed by a construction algorithm using the qualified circle or line is enclosed by the circle or line.

        Constructs a qualified circle so that the solution computed by a construction algorithm using the qualified circle or line is enclosed by the circle or line.
        """
    @staticmethod
    @overload
    def Enclosed_s(Obj : OCP.gp.gp_Circ2d) -> GccEnt_QualifiedCirc: ...
    @staticmethod
    def Enclosing_s(Obj : OCP.gp.gp_Circ2d) -> GccEnt_QualifiedCirc: 
        """
        Constructs such a qualified circle that the solution computed by a construction algorithm using the qualified circle encloses the circle.
        """
    @staticmethod
    @overload
    def Outside_s(Obj : OCP.gp.gp_Lin2d) -> GccEnt_QualifiedLin: 
        """
        Constructs a qualified line, so that the solution computed by a construction algorithm using the qualified circle or line and the circle or line are external to one another.

        Constructs a qualified circle so that the solution computed by a construction algorithm using the qualified circle or line and the circle or line are external to one another.
        """
    @staticmethod
    @overload
    def Outside_s(Obj : OCP.gp.gp_Circ2d) -> GccEnt_QualifiedCirc: ...
    @staticmethod
    @overload
    def PositionFromString_s(thePositionString : str) -> GccEnt_Position: 
        """
        Returns the position from the given string identifier (using case-insensitive comparison).

        Determines the position from the given string identifier (using case-insensitive comparison).
        """
    @staticmethod
    @overload
    def PositionFromString_s(thePositionString : str,thePosition : GccEnt_Position) -> bool: ...
    @staticmethod
    def PositionToString_s(thePosition : GccEnt_Position) -> str: 
        """
        Returns the string name for a given position.
        """
    @staticmethod
    def Print_s(thePosition : GccEnt_Position,theStream : Any) -> Any: 
        """
        Prints the name of Position type as a String on the Stream.
        """
    @staticmethod
    @overload
    def Unqualified_s(Obj : OCP.gp.gp_Lin2d) -> GccEnt_QualifiedLin: 
        """
        Constructs a qualified line, so that the relative position to the circle or line of the solution computed by a construction algorithm using the qualified circle or line is not qualified, i.e. all solutions apply.

        Constructs a qualified circle so that the relative position to the circle or line of the solution computed by a construction algorithm using the qualified circle or line is not qualified, i.e. all solutions apply.
        """
    @staticmethod
    @overload
    def Unqualified_s(Obj : OCP.gp.gp_Circ2d) -> GccEnt_QualifiedCirc: ...
    def __init__(self) -> None: ...
    pass
class GccEnt_Array1OfPosition():
    """
    Purpose: The class Array1 represents unidimensional arrays of fixed size known at run time. The range of the index is user defined. An array1 can be constructed with a "C array". This functionality is useful to call methods expecting an Array1. It allows to carry the bounds inside the arrays.
    """
    def Assign(self,theOther : GccEnt_Array1OfPosition) -> GccEnt_Array1OfPosition: 
        """
        Copies data of theOther array to this. This array should be pre-allocated and have the same length as theOther; otherwise exception Standard_DimensionMismatch is thrown.
        """
    def ChangeFirst(self) -> GccEnt_Position: 
        """
        Returns first element
        """
    def ChangeLast(self) -> GccEnt_Position: 
        """
        Returns last element
        """
    def ChangeValue(self,theIndex : int) -> GccEnt_Position: 
        """
        Variable value access
        """
    def First(self) -> GccEnt_Position: 
        """
        Returns first element
        """
    def Init(self,theValue : GccEnt_Position) -> None: 
        """
        Initialise the items with theValue
        """
    def IsAllocated(self) -> bool: 
        """
        IsAllocated flag - for naming compatibility
        """
    def IsDeletable(self) -> bool: 
        """
        myDeletable flag
        """
    def IsEmpty(self) -> bool: 
        """
        Return TRUE if array has zero length.
        """
    def Last(self) -> GccEnt_Position: 
        """
        Returns last element
        """
    def Length(self) -> int: 
        """
        Length query (the same)
        """
    def Lower(self) -> int: 
        """
        Lower bound
        """
    def Move(self,theOther : GccEnt_Array1OfPosition) -> GccEnt_Array1OfPosition: 
        """
        Move assignment. This array will borrow all the data from theOther. The moved object will keep pointer to the memory buffer and range, but it will not free the buffer on destruction.
        """
    def Resize(self,theLower : int,theUpper : int,theToCopyData : bool) -> None: 
        """
        Resizes the array to specified bounds. No re-allocation will be done if length of array does not change, but existing values will not be discarded if theToCopyData set to FALSE.
        """
    def SetValue(self,theIndex : int,theItem : GccEnt_Position) -> None: 
        """
        Set value
        """
    def Size(self) -> int: 
        """
        Size query
        """
    def Upper(self) -> int: 
        """
        Upper bound
        """
    def Value(self,theIndex : int) -> GccEnt_Position: 
        """
        Constant value access
        """
    @overload
    def __init__(self,theOther : GccEnt_Array1OfPosition) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theBegin : GccEnt_Position,theLower : int,theUpper : int) -> None: ...
    @overload
    def __init__(self,theLower : int,theUpper : int) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class GccEnt_BadQualifier(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.GccEnt', '__weakref__': <attribute '__weakref__' of 'GccEnt_BadQualifier' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'GccEnt_BadQualifier' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class GccEnt_Position():
    """
    Qualifies the position of a solution of a construction algorithm with respect to one of its arguments. This is one of the following: - GccEnt_unqualified: the position of the solution is undefined with respect to the argument, - GccEnt_enclosing: the solution encompasses the argument, - GccEnt_enclosed: the solution is encompassed by the argument, - GccEnt_outside: the solution and the argument are external to one another, - GccEnt_noqualifier: the value returned during a consultation of the qualifier when the argument is defined as GccEnt_unqualified. Note: the interior of a line or any open curve is defined as the left-hand side of the line or curve in relation to its orientation.

    Members:

      GccEnt_unqualified

      GccEnt_enclosing

      GccEnt_enclosed

      GccEnt_outside

      GccEnt_noqualifier
    """
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    GccEnt_enclosed: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_enclosed
    GccEnt_enclosing: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_enclosing
    GccEnt_noqualifier: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_noqualifier
    GccEnt_outside: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_outside
    GccEnt_unqualified: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_unqualified
    __entries: dict # value = {'GccEnt_unqualified': (GccEnt_Position.GccEnt_unqualified, None), 'GccEnt_enclosing': (GccEnt_Position.GccEnt_enclosing, None), 'GccEnt_enclosed': (GccEnt_Position.GccEnt_enclosed, None), 'GccEnt_outside': (GccEnt_Position.GccEnt_outside, None), 'GccEnt_noqualifier': (GccEnt_Position.GccEnt_noqualifier, None)}
    __members__: dict # value = {'GccEnt_unqualified': GccEnt_Position.GccEnt_unqualified, 'GccEnt_enclosing': GccEnt_Position.GccEnt_enclosing, 'GccEnt_enclosed': GccEnt_Position.GccEnt_enclosed, 'GccEnt_outside': GccEnt_Position.GccEnt_outside, 'GccEnt_noqualifier': GccEnt_Position.GccEnt_noqualifier}
    pass
class GccEnt_QualifiedCirc():
    """
    Creates a qualified 2d Circle. A qualified 2D circle is a circle (gp_Circ2d circle) with a qualifier which specifies whether the solution of a construction algorithm using the qualified circle (as an argument): - encloses the circle, or - is enclosed by the circle, or - is built so that both the circle and it are external to one another, or - is undefined (all solutions apply).
    """
    def IsEnclosed(self) -> bool: 
        """
        Returns true if the solution computed by a construction algorithm using this qualified circle is enclosed by the circle.
        """
    def IsEnclosing(self) -> bool: 
        """
        Returns true if the solution computed by a construction algorithm using this qualified circle encloses the circle.
        """
    def IsOutside(self) -> bool: 
        """
        Returns true if both the solution computed by a construction algorithm using this qualified circle and the circle are external to one another.
        """
    def IsUnqualified(self) -> bool: 
        """
        Returns true if the Circ2d is Unqualified and false in the other cases.
        """
    def Qualified(self) -> OCP.gp.gp_Circ2d: 
        """
        Returns a 2D circle to which the qualifier is assigned.
        """
    def Qualifier(self) -> GccEnt_Position: 
        """
        Returns - the qualifier of this qualified circle, if it is enclosing, enclosed or outside, or - GccEnt_noqualifier if it is unqualified.
        """
    def __init__(self,Qualified : OCP.gp.gp_Circ2d,Qualifier : GccEnt_Position) -> None: ...
    pass
class GccEnt_QualifiedLin():
    """
    Describes a qualified 2D line. A qualified 2D line is a line (gp_Lin2d line) with a qualifier which specifies whether the solution of a construction algorithm using the qualified line (as an argument): - is 'enclosed' by the line, or - is built so that both the line and it are external to one another, or - is undefined (all solutions apply). Note: the interior of a line is defined as the left-hand side of the line in relation to its orientation (i.e. when moving from the start to the end of the curve).
    """
    def IsEnclosed(self) -> bool: 
        """
        Returns true if the solution is Enclosed in the Lin2d and false in the other cases.
        """
    def IsOutside(self) -> bool: 
        """
        Returns true if the solution is Outside the Lin2d and false in the other cases.
        """
    def IsUnqualified(self) -> bool: 
        """
        Returns true if the solution is unqualified and false in the other cases.
        """
    def Qualified(self) -> OCP.gp.gp_Lin2d: 
        """
        Returns a 2D line to which the qualifier is assigned.
        """
    def Qualifier(self) -> GccEnt_Position: 
        """
        Returns the qualifier of this qualified line, if it is "enclosed" or "outside", or - GccEnt_noqualifier if it is unqualified.
        """
    def __init__(self,Qualified : OCP.gp.gp_Lin2d,Qualifier : GccEnt_Position) -> None: ...
    pass
GccEnt_enclosed: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_enclosed
GccEnt_enclosing: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_enclosing
GccEnt_noqualifier: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_noqualifier
GccEnt_outside: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_outside
GccEnt_unqualified: OCP.GccEnt.GccEnt_Position # value = GccEnt_Position.GccEnt_unqualified
