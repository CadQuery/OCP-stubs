import OCP.Hatch
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.gp
__all__  = [
"Hatch_Hatcher",
"Hatch_Line",
"Hatch_LineForm",
"Hatch_Parameter",
"Hatch_SequenceOfLine",
"Hatch_SequenceOfParameter",
"Hatch_ANYLINE",
"Hatch_XLINE",
"Hatch_YLINE"
]
class Hatch_Hatcher():
    """
    The Hatcher is an algorithm to compute cross hatchings in a 2d plane. It is mainly dedicated to display purpose.
    """
    @overload
    def AddLine(self,L : OCP.gp.gp_Lin2d,T : Hatch_LineForm=Hatch_LineForm.Hatch_ANYLINE) -> None: 
        """
        Add a line <L> to be trimmed. <T> the type is only kept from information. It is not used in the computation.

        Add an infinite line on direction <D> at distance <Dist> from the origin to be trimmed. <Dist> may be negative.
        """
    @overload
    def AddLine(self,D : OCP.gp.gp_Dir2d,Dist : float) -> None: ...
    def AddXLine(self,X : float) -> None: 
        """
        Add an infinite line parallel to the Y-axis at abciss <X>.
        """
    def AddYLine(self,Y : float) -> None: 
        """
        Add an infinite line parallel to the X-axis at ordinate <Y>.
        """
    def Coordinate(self,I : int) -> float: 
        """
        Returns the X or Y coordinate of the line of index <I> if it is a X or a Y line.
        """
    def End(self,I : int,J : int) -> float: 
        """
        Returns the last parameter of interval <J> on line <I>.
        """
    def EndIndex(self,I : int,J : int) -> Tuple[int, float]: 
        """
        Returns the last Index and Par2 of interval <J> on line <I>.
        """
    def IsXLine(self,I : int) -> bool: 
        """
        Returns True if the line of index <I> has a constant X value.

        Returns True if the line of index <I> has a constant X value.
        """
    def IsYLine(self,I : int) -> bool: 
        """
        Returns True if the line of index <I> has a constant Y value.

        Returns True if the line of index <I> has a constant Y value.
        """
    def Line(self,I : int) -> OCP.gp.gp_Lin2d: 
        """
        Returns the line of index <I>.
        """
    def LineForm(self,I : int) -> Hatch_LineForm: 
        """
        Returns the type of the line of index <I>.
        """
    @overload
    def NbIntervals(self,I : int) -> int: 
        """
        Returns the total number of intervals on all the lines.

        Returns the number of intervals on line of index <I>.
        """
    @overload
    def NbIntervals(self) -> int: ...
    def NbLines(self) -> int: 
        """
        Returns the number of lines.
        """
    def Start(self,I : int,J : int) -> float: 
        """
        Returns the first parameter of interval <J> on line <I>.
        """
    def StartIndex(self,I : int,J : int) -> Tuple[int, float]: 
        """
        Returns the first Index and Par2 of interval <J> on line <I>.
        """
    @overload
    def Tolerance(self) -> float: 
        """
        None

        None

        None

        None
        """
    @overload
    def Tolerance(self,Tol : float) -> None: ...
    @overload
    def Trim(self,L : OCP.gp.gp_Lin2d,Start : float,End : float,Index : int=0) -> None: 
        """
        Trims the lines at intersections with <L>.

        Trims the lines at intersections with <L> in the parameter range <Start>, <End>

        Trims the line at intersection with the oriented segment P1,P2.
        """
    @overload
    def Trim(self,L : OCP.gp.gp_Lin2d,Index : int=0) -> None: ...
    @overload
    def Trim(self,P1 : OCP.gp.gp_Pnt2d,P2 : OCP.gp.gp_Pnt2d,Index : int=0) -> None: ...
    def __init__(self,Tol : float,Oriented : bool=True) -> None: ...
    pass
class Hatch_Line():
    """
    Stores a Line in the Hatcher. Represented by :
    """
    def AddIntersection(self,Par1 : float,Start : bool,Index : int,Par2 : float,theToler : float) -> None: 
        """
        Insert a new intersection in the sorted list.
        """
    @overload
    def __init__(self,L : OCP.gp.gp_Lin2d,T : Hatch_LineForm) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Hatch_LineForm():
    """
    Form of a trimmed line

    Members:

      Hatch_XLINE

      Hatch_YLINE

      Hatch_ANYLINE
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
    Hatch_ANYLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_ANYLINE
    Hatch_XLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_XLINE
    Hatch_YLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_YLINE
    __entries: dict # value = {'Hatch_XLINE': (Hatch_LineForm.Hatch_XLINE, None), 'Hatch_YLINE': (Hatch_LineForm.Hatch_YLINE, None), 'Hatch_ANYLINE': (Hatch_LineForm.Hatch_ANYLINE, None)}
    __members__: dict # value = {'Hatch_XLINE': Hatch_LineForm.Hatch_XLINE, 'Hatch_YLINE': Hatch_LineForm.Hatch_YLINE, 'Hatch_ANYLINE': Hatch_LineForm.Hatch_ANYLINE}
    pass
class Hatch_Parameter():
    """
    Stores an intersection on a line represented by :
    """
    @overload
    def __init__(self,Par1 : float,Start : bool,Index : int=0,Par2 : float=0.0) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Hatch_SequenceOfLine(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : Hatch_SequenceOfLine) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : Hatch_Line) -> None: ...
    def Assign(self,theOther : Hatch_SequenceOfLine) -> Hatch_SequenceOfLine: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Hatch_Line: 
        """
        First item access
        """
    def ChangeLast(self) -> Hatch_Line: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Hatch_Line: 
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
    def First(self) -> Hatch_Line: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Hatch_Line) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Hatch_SequenceOfLine) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : Hatch_Line) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Hatch_SequenceOfLine) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Hatch_Line: 
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
    def Prepend(self,theSeq : Hatch_SequenceOfLine) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : Hatch_Line) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Hatch_Line) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Hatch_SequenceOfLine) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Hatch_Line: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Hatch_SequenceOfLine) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class Hatch_SequenceOfParameter(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : Hatch_Parameter) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : Hatch_SequenceOfParameter) -> None: ...
    def Assign(self,theOther : Hatch_SequenceOfParameter) -> Hatch_SequenceOfParameter: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> Hatch_Parameter: 
        """
        First item access
        """
    def ChangeLast(self) -> Hatch_Parameter: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> Hatch_Parameter: 
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
    def First(self) -> Hatch_Parameter: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : Hatch_Parameter) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : Hatch_SequenceOfParameter) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : Hatch_SequenceOfParameter) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : Hatch_Parameter) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> Hatch_Parameter: 
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
    def Prepend(self,theItem : Hatch_Parameter) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : Hatch_SequenceOfParameter) -> None: ...
    @overload
    def Remove(self,theFromIndex : int,theToIndex : int) -> None: 
        """
        Remove one item

        Remove range of items
        """
    @overload
    def Remove(self,theIndex : int) -> None: ...
    def Reverse(self) -> None: 
        """
        Reverse sequence
        """
    def SetValue(self,theIndex : int,theItem : Hatch_Parameter) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : Hatch_SequenceOfParameter) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> Hatch_Parameter: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : Hatch_SequenceOfParameter) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
Hatch_ANYLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_ANYLINE
Hatch_XLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_XLINE
Hatch_YLINE: OCP.Hatch.Hatch_LineForm # value = Hatch_LineForm.Hatch_YLINE
