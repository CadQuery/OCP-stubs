import OCP.TopBas
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.TopAbs
__all__  = [
"TopBas_ListOfTestInterference",
"TopBas_TestInterference"
]
class TopBas_ListOfTestInterference(OCP.NCollection.NCollection_BaseList):
    """
    Purpose: Simple list to link items together keeping the first and the last one. Inherits BaseList, adding the data item to each node.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : TopBas_TestInterference,theIter : Any) -> None: 
        """
        Append one item at the end

        Append one item at the end and output iterator pointing at the appended item

        Append another list at the end. After this operation, theOther list will be cleared.
        """
    @overload
    def Append(self,theItem : TopBas_TestInterference) -> TopBas_TestInterference: ...
    @overload
    def Append(self,theOther : TopBas_ListOfTestInterference) -> None: ...
    def Assign(self,theOther : TopBas_ListOfTestInterference) -> TopBas_ListOfTestInterference: 
        """
        Replace this list by the items of another list (theOther parameter). This method does not change the internal allocator.
        """
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: 
        """
        Clear this list
        """
    def Extent(self) -> int: 
        """
        None
        """
    def First(self) -> TopBas_TestInterference: 
        """
        First item

        First item (non-const)
        """
    @overload
    def InsertAfter(self,theItem : TopBas_TestInterference,theIter : Any) -> TopBas_TestInterference: 
        """
        InsertAfter

        InsertAfter
        """
    @overload
    def InsertAfter(self,theOther : TopBas_ListOfTestInterference,theIter : Any) -> None: ...
    @overload
    def InsertBefore(self,theItem : TopBas_TestInterference,theIter : Any) -> TopBas_TestInterference: 
        """
        InsertBefore

        InsertBefore
        """
    @overload
    def InsertBefore(self,theOther : TopBas_ListOfTestInterference,theIter : Any) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        None
        """
    def Last(self) -> TopBas_TestInterference: 
        """
        Last item

        Last item (non-const)
        """
    @overload
    def Prepend(self,theOther : TopBas_ListOfTestInterference) -> None: 
        """
        Prepend one item at the beginning

        Prepend another list at the beginning
        """
    @overload
    def Prepend(self,theItem : TopBas_TestInterference) -> TopBas_TestInterference: ...
    def Remove(self,theIter : Any) -> None: 
        """
        Remove item pointed by iterator theIter; theIter is then set to the next item
        """
    def RemoveFirst(self) -> None: 
        """
        RemoveFirst item
        """
    def Reverse(self) -> None: 
        """
        Reverse the list
        """
    def Size(self) -> int: 
        """
        Size - Number of items
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : TopBas_ListOfTestInterference) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    pass
class TopBas_TestInterference():
    """
    None
    """
    @overload
    def Boundary(self) -> int: 
        """
        None

        None
        """
    @overload
    def Boundary(self,B : int) -> None: ...
    @overload
    def BoundaryTransition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def BoundaryTransition(self,BTr : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def Intersection(self,I : float) -> None: 
        """
        None

        None
        """
    @overload
    def Intersection(self) -> float: ...
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Orientation(self,O : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def Transition(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        None

        None
        """
    @overload
    def Transition(self,Tr : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def __init__(self,Inters : float,Bound : int,Orient : OCP.TopAbs.TopAbs_Orientation,Trans : OCP.TopAbs.TopAbs_Orientation,BTrans : OCP.TopAbs.TopAbs_Orientation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @property
    def ChangeBoundary(self) -> int:
        """
        None

        :type: int
        """
    @ChangeBoundary.setter
    def ChangeBoundary(self, arg1: int) -> None:
        """
        None
        """
    @property
    def ChangeIntersection(self) -> float:
        """
        None

        :type: float
        """
    @ChangeIntersection.setter
    def ChangeIntersection(self, arg1: float) -> None:
        """
        None
        """
    pass
