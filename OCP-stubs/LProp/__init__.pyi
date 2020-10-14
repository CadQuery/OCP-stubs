import OCP.LProp
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.GeomAbs
__all__  = [
"LProp_AnalyticCurInf",
"LProp_BadContinuity",
"LProp_CIType",
"LProp_CurAndInf",
"LProp_NotDefined",
"LProp_SequenceOfCIType",
"LProp_Status",
"LProp_Computed",
"LProp_Defined",
"LProp_Inflection",
"LProp_MaxCur",
"LProp_MinCur",
"LProp_Undecided",
"LProp_Undefined"
]
class LProp_AnalyticCurInf():
    """
    Computes the locals extremas of curvature of a gp curve Remark : a gp curve has not inflection.
    """
    def Perform(self,T : OCP.GeomAbs.GeomAbs_CurveType,UFirst : float,ULast : float,Result : LProp_CurAndInf) -> None: 
        """
        None
        """
    def __init__(self) -> None: ...
    pass
class LProp_BadContinuity(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.LProp', '__weakref__': <attribute '__weakref__' of 'LProp_BadContinuity' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'LProp_BadContinuity' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class LProp_CIType():
    """
    Identifies the type of a particular point on a curve: - LProp_Inflection: a point of inflection - LProp_MinCur: a minimum of curvature - LProp_MaxCur: a maximum of curvature.

    Members:

      LProp_Inflection

      LProp_MinCur

      LProp_MaxCur
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    LProp_Inflection: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_Inflection
    LProp_MaxCur: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_MaxCur
    LProp_MinCur: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_MinCur
    __entries: dict # value = {'LProp_Inflection': (LProp_CIType.LProp_Inflection, None), 'LProp_MinCur': (LProp_CIType.LProp_MinCur, None), 'LProp_MaxCur': (LProp_CIType.LProp_MaxCur, None)}
    __members__: dict # value = {'LProp_Inflection': LProp_CIType.LProp_Inflection, 'LProp_MinCur': LProp_CIType.LProp_MinCur, 'LProp_MaxCur': LProp_CIType.LProp_MaxCur}
    pass
class LProp_CurAndInf():
    """
    Stores the parameters of a curve 2d or 3d corresponding to the curvature's extremas and the Inflection's Points.
    """
    def AddExtCur(self,Param : float,IsMin : bool) -> None: 
        """
        None
        """
    def AddInflection(self,Param : float) -> None: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of points. The Points are stored to increasing parameter.
        """
    def Parameter(self,N : int) -> float: 
        """
        Returns the parameter of the Nth point. raises if N not in the range [1,NbPoints()]
        """
    def Type(self,N : int) -> LProp_CIType: 
        """
        Returns - MinCur if the Nth parameter corresponds to a minimum of the radius of curvature. - MaxCur if the Nth parameter corresponds to a maximum of the radius of curvature. - Inflection if the parameter corresponds to a point of inflection. raises if N not in the range [1,NbPoints()]
        """
    def __init__(self) -> None: ...
    pass
class LProp_NotDefined(Exception, BaseException):
    class type():
        pass
    __cause__: getset_descriptor # value = <attribute '__cause__' of 'BaseException' objects>
    __context__: getset_descriptor # value = <attribute '__context__' of 'BaseException' objects>
    __dict__: mappingproxy # value = mappingproxy({'__module__': 'OCP.LProp', '__weakref__': <attribute '__weakref__' of 'LProp_NotDefined' objects>, '__doc__': None})
    __suppress_context__: member_descriptor # value = <member '__suppress_context__' of 'BaseException' objects>
    __traceback__: getset_descriptor # value = <attribute '__traceback__' of 'BaseException' objects>
    __weakref__: getset_descriptor # value = <attribute '__weakref__' of 'LProp_NotDefined' objects>
    args: getset_descriptor # value = <attribute 'args' of 'BaseException' objects>
    pass
class LProp_SequenceOfCIType(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : LProp_CIType) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : LProp_SequenceOfCIType) -> None: ...
    def Assign(self,theOther : LProp_SequenceOfCIType) -> LProp_SequenceOfCIType: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> LProp_CIType: 
        """
        First item access
        """
    def ChangeLast(self) -> LProp_CIType: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> LProp_CIType: 
        """
        Variable item access by theIndex
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear the items out, take a new allocator if non null
        """
    def Exchange(self,I : int,J : int) -> None: 
        """
        Exchange two members
        """
    def First(self) -> LProp_CIType: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : LProp_SequenceOfCIType) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : LProp_CIType) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : LProp_SequenceOfCIType) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : LProp_CIType) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> LProp_CIType: 
        """
        Last item access
        """
    def Length(self) -> int: 
        """
        Number of items
        """
    def Lower(self) -> int: 
        """
        Method for consistency with other collections.
        """
    @overload
    def Prepend(self,theItem : LProp_CIType) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : LProp_SequenceOfCIType) -> None: ...
    @overload
    def Remove(self,theIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : LProp_CIType) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : LProp_SequenceOfCIType) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> LProp_CIType: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : LProp_SequenceOfCIType) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class LProp_Status():
    """
    None

    Members:

      LProp_Undecided

      LProp_Undefined

      LProp_Defined

      LProp_Computed
    """
    def __index__(self) -> int: ...
    def __init__(self,arg0 : int) -> None: ...
    def __int__(self) -> int: ...
    @property
    def name(self) -> str:
        """
        (self: handle) -> str

        :type: str
        """
    LProp_Computed: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Computed
    LProp_Defined: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Defined
    LProp_Undecided: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Undecided
    LProp_Undefined: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Undefined
    __entries: dict # value = {'LProp_Undecided': (LProp_Status.LProp_Undecided, None), 'LProp_Undefined': (LProp_Status.LProp_Undefined, None), 'LProp_Defined': (LProp_Status.LProp_Defined, None), 'LProp_Computed': (LProp_Status.LProp_Computed, None)}
    __members__: dict # value = {'LProp_Undecided': LProp_Status.LProp_Undecided, 'LProp_Undefined': LProp_Status.LProp_Undefined, 'LProp_Defined': LProp_Status.LProp_Defined, 'LProp_Computed': LProp_Status.LProp_Computed}
    pass
LProp_Computed: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Computed
LProp_Defined: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Defined
LProp_Inflection: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_Inflection
LProp_MaxCur: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_MaxCur
LProp_MinCur: OCP.LProp.LProp_CIType # value = LProp_CIType.LProp_MinCur
LProp_Undecided: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Undecided
LProp_Undefined: OCP.LProp.LProp_Status # value = LProp_Status.LProp_Undefined
