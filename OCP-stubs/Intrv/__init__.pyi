import OCP.Intrv
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
__all__  = [
"Intrv_Interval",
"Intrv_Intervals",
"Intrv_Position",
"Intrv_SequenceOfInterval",
"AreFused",
"Intrv_After",
"Intrv_Before",
"Intrv_Enclosing",
"Intrv_Inside",
"Intrv_JustAfter",
"Intrv_JustBefore",
"Intrv_JustEnclosingAtEnd",
"Intrv_JustEnclosingAtStart",
"Intrv_JustOverlappingAtEnd",
"Intrv_JustOverlappingAtStart",
"Intrv_OverlappingAtEnd",
"Intrv_OverlappingAtStart",
"Intrv_Similar"
]
class Intrv_Interval():
    """
    **-----------**** Other ***---* IsBefore ***----------* IsJustBefore ***---------------* IsOverlappingAtStart ***------------------------* IsJustEnclosingAtEnd ***-----------------------------------* IsEnclosing ***----* IsJustOverlappingAtStart ***-------------* IsSimilar ***------------------------* IsJustEnclosingAtStart ***-* IsInside ***------* IsJustOverlappingAtEnd ***-----------------* IsOverlappingAtEnd ***--------* IsJustAfter ***---* IsAfter
    """
    def Bounds(self,TolStart : float,TolEnd : float) -> Tuple[float, float]: 
        """
        None

        None
        """
    def CutAtEnd(self,End : float,TolEnd : float) -> None: 
        """
        <-----****+**** Old one **+**------> Tool for cutting <<< <<< <-----****+**** result

        <-----****+**** Old one **+**------> Tool for cutting <<< <<< <-----****+**** result
        """
    def CutAtStart(self,Start : float,TolStart : float) -> None: 
        """
        ****+****-----------> Old one <----------**+** Tool for cutting >>> >>> ****+****-----------> result

        ****+****-----------> Old one <----------**+** Tool for cutting >>> >>> ****+****-----------> result
        """
    def End(self) -> float: 
        """
        None

        None
        """
    def FuseAtEnd(self,End : float,TolEnd : float) -> None: 
        """
        <---------------------****+**** Old one <-----------------**+** New one to fuse >>> >>> <---------------------****+**** result

        <---------------------****+**** Old one <-----------------**+** New one to fuse >>> >>> <---------------------****+**** result
        """
    def FuseAtStart(self,Start : float,TolStart : float) -> None: 
        """
        ****+****--------------------> Old one ****+****------------------------> New one to fuse <<< <<< ****+****------------------------> result

        ****+****--------------------> Old one ****+****------------------------> New one to fuse <<< <<< ****+****------------------------> result
        """
    def IsAfter(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is After Other **-----------**** me ***----------------** Other

        True if me is After Other **-----------**** me ***----------------** Other
        """
    def IsBefore(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is Before Other ***----------------** me **-----------**** Other

        True if me is Before Other ***----------------** me **-----------**** Other
        """
    def IsEnclosing(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is Enclosing Other ***----------------------------**** me ***------------------** Other

        True if me is Enclosing Other ***----------------------------**** me ***------------------** Other
        """
    def IsInside(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is Inside Other **-----------**** me ***--------------------------** Other

        True if me is Inside Other **-----------**** me ***--------------------------** Other
        """
    def IsJustAfter(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just after Other ****-------**** me ***-----------** Other

        True if me is just after Other ****-------**** me ***-----------** Other
        """
    def IsJustBefore(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just before Other ***--------**** me ***-----------** Other

        True if me is just before Other ***--------**** me ***-----------** Other
        """
    def IsJustEnclosingAtEnd(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just Enclosing Other at End ***----------------------------**** me ***-----------------**** Other

        True if me is just Enclosing Other at End ***----------------------------**** me ***-----------------**** Other
        """
    def IsJustEnclosingAtStart(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just Enclosing Other at start ***---------------------------**** me ***------------------** Other

        True if me is just Enclosing Other at start ***---------------------------**** me ***------------------** Other
        """
    def IsJustOverlappingAtEnd(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just overlapping Other at end ***-----------* me ***------------------------** Other

        True if me is just overlapping Other at end ***-----------* me ***------------------------** Other
        """
    def IsJustOverlappingAtStart(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is just overlapping Other at start ***-----------*** me ***------------------------** Other

        True if me is just overlapping Other at start ***-----------*** me ***------------------------** Other
        """
    def IsOverlappingAtEnd(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is overlapping Other at end ***-----------** me ***---------------*** Other

        True if me is overlapping Other at end ***-----------** me ***---------------*** Other
        """
    def IsOverlappingAtStart(self,Other : Intrv_Interval) -> bool: 
        """
        True if me is overlapping Other at start ***---------------*** me ***-----------** Other

        True if me is overlapping Other at start ***---------------*** me ***-----------** Other
        """
    def IsProbablyEmpty(self) -> bool: 
        """
        True if myStart+myTolStart > myEnd-myTolEnd or if myEnd+myTolEnd > myStart-myTolStart

        True if myStart+myTolStart > myEnd-myTolEnd or if myEnd+myTolEnd > myStart-myTolStart
        """
    def IsSimilar(self,Other : Intrv_Interval) -> bool: 
        """
        True if me and Other have the same bounds *----------------*** me ***-----------------** Other

        True if me and Other have the same bounds *----------------*** me ***-----------------** Other
        """
    def Position(self,Other : Intrv_Interval) -> Intrv_Position: 
        """
        True if me is Before Other **-----------**** Other ***-----* Before ***------------* JustBefore ***-----------------* OverlappingAtStart ***--------------------------* JustEnclosingAtEnd ***-------------------------------------* Enclosing ***----* JustOverlappingAtStart ***-------------* Similar ***------------------------* JustEnclosingAtStart ***-* Inside ***------* JustOverlappingAtEnd ***-----------------* OverlappingAtEnd ***--------* JustAfter ***---* After
        """
    def SetEnd(self,End : float,TolEnd : float) -> None: 
        """
        None

        None
        """
    def SetStart(self,Start : float,TolStart : float) -> None: 
        """
        None

        None
        """
    def Start(self) -> float: 
        """
        None

        None
        """
    def TolEnd(self) -> float: 
        """
        None

        None
        """
    def TolStart(self) -> float: 
        """
        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Start : float,End : float) -> None: ...
    @overload
    def __init__(self,Start : float,TolStart : float,End : float,TolEnd : float) -> None: ...
    pass
class Intrv_Intervals():
    """
    The class Intervals is a sorted sequence of non overlapping Real Intervals.
    """
    @overload
    def Intersect(self,Tool : Intrv_Intervals) -> None: 
        """
        Intersects the intervals with the interval <Tool>.

        Intersects the intervals with the intervals in the sequence <Tool>.
        """
    @overload
    def Intersect(self,Tool : Intrv_Interval) -> None: ...
    def NbIntervals(self) -> int: 
        """
        None

        None
        """
    @overload
    def Subtract(self,Tool : Intrv_Interval) -> None: 
        """
        None

        None
        """
    @overload
    def Subtract(self,Tool : Intrv_Intervals) -> None: ...
    @overload
    def Unite(self,Tool : Intrv_Interval) -> None: 
        """
        None

        None
        """
    @overload
    def Unite(self,Tool : Intrv_Intervals) -> None: ...
    def Value(self,Index : int) -> Intrv_Interval: 
        """
        None

        None
        """
    @overload
    def XUnite(self,Tool : Intrv_Intervals) -> None: 
        """
        None

        None
        """
    @overload
    def XUnite(self,Tool : Intrv_Interval) -> None: ...
    @overload
    def __init__(self,Int : Intrv_Intervals) -> None: ...
    @overload
    def __init__(self,Int : Intrv_Interval) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Intrv_Position():
    """
    None

    Members:

      Intrv_Before

      Intrv_JustBefore

      Intrv_OverlappingAtStart

      Intrv_JustEnclosingAtEnd

      Intrv_Enclosing

      Intrv_JustOverlappingAtStart

      Intrv_Similar

      Intrv_JustEnclosingAtStart

      Intrv_Inside

      Intrv_JustOverlappingAtEnd

      Intrv_OverlappingAtEnd

      Intrv_JustAfter

      Intrv_After
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
    Intrv_After: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_After
    Intrv_Before: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Before
    Intrv_Enclosing: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Enclosing
    Intrv_Inside: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Inside
    Intrv_JustAfter: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustAfter
    Intrv_JustBefore: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustBefore
    Intrv_JustEnclosingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustEnclosingAtEnd
    Intrv_JustEnclosingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustEnclosingAtStart
    Intrv_JustOverlappingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustOverlappingAtEnd
    Intrv_JustOverlappingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustOverlappingAtStart
    Intrv_OverlappingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_OverlappingAtEnd
    Intrv_OverlappingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_OverlappingAtStart
    Intrv_Similar: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Similar
    __entries: dict # value = {'Intrv_Before': (Intrv_Position.Intrv_Before, None), 'Intrv_JustBefore': (Intrv_Position.Intrv_JustBefore, None), 'Intrv_OverlappingAtStart': (Intrv_Position.Intrv_OverlappingAtStart, None), 'Intrv_JustEnclosingAtEnd': (Intrv_Position.Intrv_JustEnclosingAtEnd, None), 'Intrv_Enclosing': (Intrv_Position.Intrv_Enclosing, None), 'Intrv_JustOverlappingAtStart': (Intrv_Position.Intrv_JustOverlappingAtStart, None), 'Intrv_Similar': (Intrv_Position.Intrv_Similar, None), 'Intrv_JustEnclosingAtStart': (Intrv_Position.Intrv_JustEnclosingAtStart, None), 'Intrv_Inside': (Intrv_Position.Intrv_Inside, None), 'Intrv_JustOverlappingAtEnd': (Intrv_Position.Intrv_JustOverlappingAtEnd, None), 'Intrv_OverlappingAtEnd': (Intrv_Position.Intrv_OverlappingAtEnd, None), 'Intrv_JustAfter': (Intrv_Position.Intrv_JustAfter, None), 'Intrv_After': (Intrv_Position.Intrv_After, None)}
    __members__: dict # value = {'Intrv_Before': Intrv_Position.Intrv_Before, 'Intrv_JustBefore': Intrv_Position.Intrv_JustBefore, 'Intrv_OverlappingAtStart': Intrv_Position.Intrv_OverlappingAtStart, 'Intrv_JustEnclosingAtEnd': Intrv_Position.Intrv_JustEnclosingAtEnd, 'Intrv_Enclosing': Intrv_Position.Intrv_Enclosing, 'Intrv_JustOverlappingAtStart': Intrv_Position.Intrv_JustOverlappingAtStart, 'Intrv_Similar': Intrv_Position.Intrv_Similar, 'Intrv_JustEnclosingAtStart': Intrv_Position.Intrv_JustEnclosingAtStart, 'Intrv_Inside': Intrv_Position.Intrv_Inside, 'Intrv_JustOverlappingAtEnd': Intrv_Position.Intrv_JustOverlappingAtEnd, 'Intrv_OverlappingAtEnd': Intrv_Position.Intrv_OverlappingAtEnd, 'Intrv_JustAfter': Intrv_Position.Intrv_JustAfter, 'Intrv_After': Intrv_Position.Intrv_After}
    pass
class Intrv_SequenceOfInterval(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Intrv_SequenceOfInterval) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Intrv_Interval) -> None: ...
    def Assign(self,theOther : Intrv_SequenceOfInterval) -> Intrv_SequenceOfInterval: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Intrv_Interval: 
        """
        First item access
        """
    def ChangeLast(self) -> Intrv_Interval: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Intrv_Interval: 
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
    def First(self) -> Intrv_Interval: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Intrv_SequenceOfInterval) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Intrv_Interval) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Intrv_Interval) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Intrv_SequenceOfInterval) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Intrv_Interval: 
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
    def Prepend(self,theSeq : Intrv_SequenceOfInterval) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Intrv_Interval) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : Intrv_Interval) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Intrv_SequenceOfInterval) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Intrv_Interval: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : Intrv_SequenceOfInterval) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
def AreFused(c1 : float,t1 : float,c2 : float,t2 : float) -> bool:
    """
    None
    """
Intrv_After: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_After
Intrv_Before: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Before
Intrv_Enclosing: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Enclosing
Intrv_Inside: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Inside
Intrv_JustAfter: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustAfter
Intrv_JustBefore: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustBefore
Intrv_JustEnclosingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustEnclosingAtEnd
Intrv_JustEnclosingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustEnclosingAtStart
Intrv_JustOverlappingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustOverlappingAtEnd
Intrv_JustOverlappingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_JustOverlappingAtStart
Intrv_OverlappingAtEnd: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_OverlappingAtEnd
Intrv_OverlappingAtStart: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_OverlappingAtStart
Intrv_Similar: OCP.Intrv.Intrv_Position # value = Intrv_Position.Intrv_Similar
