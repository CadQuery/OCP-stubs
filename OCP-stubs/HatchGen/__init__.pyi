import OCP.HatchGen
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.IntRes2d
import OCP.TopAbs
__all__  = [
"HatchGen_Domain",
"HatchGen_Domains",
"HatchGen_ErrorStatus",
"HatchGen_IntersectionPoint",
"HatchGen_IntersectionType",
"HatchGen_PointOnElement",
"HatchGen_PointOnHatching",
"HatchGen_PointsOnElement",
"HatchGen_PointsOnHatching",
"HatchGen_IncoherentParity",
"HatchGen_IncompatibleStates",
"HatchGen_NoProblem",
"HatchGen_TANGENT",
"HatchGen_TOUCH",
"HatchGen_TRUE",
"HatchGen_TransitionFailure",
"HatchGen_TrimFailure",
"HatchGen_UNDETERMINED"
]
class HatchGen_Domain():
    """
    None
    """
    def Dump(self,Index : int=0) -> None: 
        """
        Dump of the domain.
        """
    def FirstPoint(self) -> HatchGen_PointOnHatching: 
        """
        Returns the first point of the domain. The exception DomainError is raised if HasFirstPoint returns False.

        Returns the first point of the domain. The exception DomainError is raised if HasFirstPoint returns False.
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the domain has a first point.

        Returns True if the domain has a first point.
        """
    def HasSecondPoint(self) -> bool: 
        """
        Returns True if the domain has a second point.

        Returns True if the domain has a second point.
        """
    def SecondPoint(self) -> HatchGen_PointOnHatching: 
        """
        Returns the second point of the domain. The exception DomainError is raised if HasSecondPoint returns False.

        Returns the second point of the domain. The exception DomainError is raised if HasSecondPoint returns False.
        """
    @overload
    def SetFirstPoint(self,P : HatchGen_PointOnHatching) -> None: 
        """
        Sets the first point of the domain.

        Sets the first point of the domain at the infinite.

        Sets the first point of the domain.

        Sets the first point of the domain at the infinite.
        """
    @overload
    def SetFirstPoint(self) -> None: ...
    @overload
    def SetPoints(self) -> None: 
        """
        Sets the first and the second points of the domain.

        Sets the first and the second points of the domain as the infinite.

        Sets the first and the second points of the domain.

        Sets the first and the second points of the domain as the infinite.
        """
    @overload
    def SetPoints(self,P1 : HatchGen_PointOnHatching,P2 : HatchGen_PointOnHatching) -> None: ...
    @overload
    def SetSecondPoint(self) -> None: 
        """
        Sets the second point of the domain.

        Sets the second point of the domain at the infinite.

        Sets the second point of the domain.

        Sets the second point of the domain at the infinite.
        """
    @overload
    def SetSecondPoint(self,P : HatchGen_PointOnHatching) -> None: ...
    @overload
    def __init__(self,P : HatchGen_PointOnHatching,First : bool) -> None: ...
    @overload
    def __init__(self,P1 : HatchGen_PointOnHatching,P2 : HatchGen_PointOnHatching) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class HatchGen_Domains(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HatchGen_Domain) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : HatchGen_Domains) -> None: ...
    def Assign(self,theOther : HatchGen_Domains) -> HatchGen_Domains: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> HatchGen_Domain: 
        """
        First item access
        """
    def ChangeLast(self) -> HatchGen_Domain: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> HatchGen_Domain: 
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
    def First(self) -> HatchGen_Domain: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : HatchGen_Domains) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : HatchGen_Domain) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : HatchGen_Domains) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : HatchGen_Domain) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> HatchGen_Domain: 
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
    def Prepend(self,theSeq : HatchGen_Domains) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : HatchGen_Domain) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : HatchGen_Domain) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : HatchGen_Domains) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> HatchGen_Domain: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : HatchGen_Domains) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class HatchGen_ErrorStatus():
    """
    Error status.

    Members:

      HatchGen_NoProblem

      HatchGen_TrimFailure

      HatchGen_TransitionFailure

      HatchGen_IncoherentParity

      HatchGen_IncompatibleStates
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    HatchGen_IncoherentParity: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_IncoherentParity: 3>
    HatchGen_IncompatibleStates: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_IncompatibleStates: 4>
    HatchGen_NoProblem: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_NoProblem: 0>
    HatchGen_TransitionFailure: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_TransitionFailure: 2>
    HatchGen_TrimFailure: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_TrimFailure: 1>
    __entries: dict # value = {'HatchGen_NoProblem': (<HatchGen_ErrorStatus.HatchGen_NoProblem: 0>, None), 'HatchGen_TrimFailure': (<HatchGen_ErrorStatus.HatchGen_TrimFailure: 1>, None), 'HatchGen_TransitionFailure': (<HatchGen_ErrorStatus.HatchGen_TransitionFailure: 2>, None), 'HatchGen_IncoherentParity': (<HatchGen_ErrorStatus.HatchGen_IncoherentParity: 3>, None), 'HatchGen_IncompatibleStates': (<HatchGen_ErrorStatus.HatchGen_IncompatibleStates: 4>, None)}
    __members__: dict # value = {'HatchGen_NoProblem': <HatchGen_ErrorStatus.HatchGen_NoProblem: 0>, 'HatchGen_TrimFailure': <HatchGen_ErrorStatus.HatchGen_TrimFailure: 1>, 'HatchGen_TransitionFailure': <HatchGen_ErrorStatus.HatchGen_TransitionFailure: 2>, 'HatchGen_IncoherentParity': <HatchGen_ErrorStatus.HatchGen_IncoherentParity: 3>, 'HatchGen_IncompatibleStates': <HatchGen_ErrorStatus.HatchGen_IncompatibleStates: 4>}
    pass
class HatchGen_IntersectionPoint():
    """
    None
    """
    def Dump(self,Index : int=0) -> None: 
        """
        Dump of the point on element.
        """
    def Index(self) -> int: 
        """
        Returns the index of the supporting curve.
        """
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve.
        """
    def Position(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the position of the point on the curve.
        """
    def SegmentBeginning(self) -> bool: 
        """
        Returns the flag that the point is the beginning of a segment.
        """
    def SegmentEnd(self) -> bool: 
        """
        Returns the flag that the point is the end of a segment.
        """
    def SetIndex(self,Index : int) -> None: 
        """
        Sets the index of the supporting curve.
        """
    def SetParameter(self,Parameter : float) -> None: 
        """
        Sets the parameter on the curve.
        """
    def SetPosition(self,Position : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets the position of the point on the curve.
        """
    def SetSegmentBeginning(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the beginning of a segment.
        """
    def SetSegmentEnd(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the end of a segment.
        """
    def SetStateAfter(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state after the intersection.
        """
    def SetStateBefore(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state before the intersection.
        """
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state after of the intersection.
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state before the intersection.
        """
    pass
class HatchGen_IntersectionType():
    """
    Intersection type between the hatching and the element.

    Members:

      HatchGen_TRUE

      HatchGen_TOUCH

      HatchGen_TANGENT

      HatchGen_UNDETERMINED
    """
    def __eq__(self,other : object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __init__(self,value : int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self,other : object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self,state : int) -> None: ...
    @property
    def name(self) -> None:
        """
        :type: None
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    HatchGen_TANGENT: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TANGENT: 2>
    HatchGen_TOUCH: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TOUCH: 1>
    HatchGen_TRUE: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TRUE: 0>
    HatchGen_UNDETERMINED: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_UNDETERMINED: 3>
    __entries: dict # value = {'HatchGen_TRUE': (<HatchGen_IntersectionType.HatchGen_TRUE: 0>, None), 'HatchGen_TOUCH': (<HatchGen_IntersectionType.HatchGen_TOUCH: 1>, None), 'HatchGen_TANGENT': (<HatchGen_IntersectionType.HatchGen_TANGENT: 2>, None), 'HatchGen_UNDETERMINED': (<HatchGen_IntersectionType.HatchGen_UNDETERMINED: 3>, None)}
    __members__: dict # value = {'HatchGen_TRUE': <HatchGen_IntersectionType.HatchGen_TRUE: 0>, 'HatchGen_TOUCH': <HatchGen_IntersectionType.HatchGen_TOUCH: 1>, 'HatchGen_TANGENT': <HatchGen_IntersectionType.HatchGen_TANGENT: 2>, 'HatchGen_UNDETERMINED': <HatchGen_IntersectionType.HatchGen_UNDETERMINED: 3>}
    pass
class HatchGen_PointOnElement(HatchGen_IntersectionPoint):
    """
    None
    """
    def Dump(self,Index : int=0) -> None: 
        """
        Dump of the point on element.
        """
    def Index(self) -> int: 
        """
        Returns the index of the supporting curve.
        """
    def IntersectionType(self) -> HatchGen_IntersectionType: 
        """
        Returns the intersection type at this point.

        Returns the intersection type at this point.
        """
    def IsDifferent(self,Point : HatchGen_PointOnElement,Confusion : float) -> bool: 
        """
        Tests if the point is different from an other.
        """
    def IsIdentical(self,Point : HatchGen_PointOnElement,Confusion : float) -> bool: 
        """
        Tests if the point is identical to an other. That is to say : P1.myIndex = P2.myIndex Abs (P1.myParam - P2.myParam) <= Confusion P1.myPosit = P2.myPosit P1.myBefore = P2.myBefore P1.myAfter = P2.myAfter P1.mySegBeg = P2.mySegBeg P1.mySegEnd = P2.mySegEnd P1.myType = P2.myType
        """
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve.
        """
    def Position(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the position of the point on the curve.
        """
    def SegmentBeginning(self) -> bool: 
        """
        Returns the flag that the point is the beginning of a segment.
        """
    def SegmentEnd(self) -> bool: 
        """
        Returns the flag that the point is the end of a segment.
        """
    def SetIndex(self,Index : int) -> None: 
        """
        Sets the index of the supporting curve.
        """
    def SetIntersectionType(self,Type : HatchGen_IntersectionType) -> None: 
        """
        Sets the intersection type at this point.

        Sets the intersection type at this point.
        """
    def SetParameter(self,Parameter : float) -> None: 
        """
        Sets the parameter on the curve.
        """
    def SetPosition(self,Position : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets the position of the point on the curve.
        """
    def SetSegmentBeginning(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the beginning of a segment.
        """
    def SetSegmentEnd(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the end of a segment.
        """
    def SetStateAfter(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state after the intersection.
        """
    def SetStateBefore(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state before the intersection.
        """
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state after of the intersection.
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state before the intersection.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Point : OCP.IntRes2d.IntRes2d_IntersectionPoint) -> None: ...
    pass
class HatchGen_PointOnHatching(HatchGen_IntersectionPoint):
    """
    None
    """
    def AddPoint(self,Point : HatchGen_PointOnElement,Confusion : float) -> None: 
        """
        Adds a point on element to the point.
        """
    def ClrPoints(self) -> None: 
        """
        Removes all the points on element of the point.
        """
    def Dump(self,Index : int=0) -> None: 
        """
        Dump of the point.
        """
    def Index(self) -> int: 
        """
        Returns the index of the supporting curve.
        """
    def IsEqual(self,Point : HatchGen_PointOnHatching,Confusion : float) -> bool: 
        """
        Tests if the point is equal to an other. A point on hatching P1 is said to be equal to an other P2 if : | P2.myParam - P1.myParam | <= Confusion
        """
    def IsGreater(self,Point : HatchGen_PointOnHatching,Confusion : float) -> bool: 
        """
        Tests if the point is greater than an other. A point on hatching P1 is said to be greater than an other P2 if : P1.myParam - P2.myParam > Confusion
        """
    def IsLower(self,Point : HatchGen_PointOnHatching,Confusion : float) -> bool: 
        """
        Tests if the point is lower than an other. A point on hatching P1 is said to be lower than an other P2 if : P2.myParam - P1.myParam > Confusion
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of elements intersecting the hatching at this point.
        """
    def Parameter(self) -> float: 
        """
        Returns the parameter on the curve.
        """
    def Point(self,Index : int) -> HatchGen_PointOnElement: 
        """
        Returns the Index-th point on element of the point. The exception OutOfRange is raised if Index > NbPoints.
        """
    def Position(self) -> OCP.TopAbs.TopAbs_Orientation: 
        """
        Returns the position of the point on the curve.
        """
    def RemPoint(self,Index : int) -> None: 
        """
        Removes the Index-th point on element of the point. The exception OutOfRange is raised if Index > NbPoints.
        """
    def SegmentBeginning(self) -> bool: 
        """
        Returns the flag that the point is the beginning of a segment.
        """
    def SegmentEnd(self) -> bool: 
        """
        Returns the flag that the point is the end of a segment.
        """
    def SetIndex(self,Index : int) -> None: 
        """
        Sets the index of the supporting curve.
        """
    def SetParameter(self,Parameter : float) -> None: 
        """
        Sets the parameter on the curve.
        """
    def SetPosition(self,Position : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets the position of the point on the curve.
        """
    def SetSegmentBeginning(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the beginning of a segment.
        """
    def SetSegmentEnd(self,State : bool=True) -> None: 
        """
        Sets the flag that the point is the end of a segment.
        """
    def SetStateAfter(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state after the intersection.
        """
    def SetStateBefore(self,State : OCP.TopAbs.TopAbs_State) -> None: 
        """
        Sets the transition state before the intersection.
        """
    def StateAfter(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state after of the intersection.
        """
    def StateBefore(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the transition state before the intersection.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Point : OCP.IntRes2d.IntRes2d_IntersectionPoint) -> None: ...
    pass
class HatchGen_PointsOnElement(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HatchGen_PointOnElement) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : HatchGen_PointsOnElement) -> None: ...
    def Assign(self,theOther : HatchGen_PointsOnElement) -> HatchGen_PointsOnElement: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> HatchGen_PointOnElement: 
        """
        First item access
        """
    def ChangeLast(self) -> HatchGen_PointOnElement: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> HatchGen_PointOnElement: 
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
    def First(self) -> HatchGen_PointOnElement: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : HatchGen_PointsOnElement) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : HatchGen_PointOnElement) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : HatchGen_PointOnElement) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : HatchGen_PointsOnElement) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> HatchGen_PointOnElement: 
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
    def Prepend(self,theSeq : HatchGen_PointsOnElement) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : HatchGen_PointOnElement) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : HatchGen_PointOnElement) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : HatchGen_PointsOnElement) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> HatchGen_PointOnElement: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self,theOther : HatchGen_PointsOnElement) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class HatchGen_PointsOnHatching(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : HatchGen_PointOnHatching) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : HatchGen_PointsOnHatching) -> None: ...
    def Assign(self,theOther : HatchGen_PointsOnHatching) -> HatchGen_PointsOnHatching: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> HatchGen_PointOnHatching: 
        """
        First item access
        """
    def ChangeLast(self) -> HatchGen_PointOnHatching: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> HatchGen_PointOnHatching: 
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
    def First(self) -> HatchGen_PointOnHatching: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : HatchGen_PointsOnHatching) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : HatchGen_PointOnHatching) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : HatchGen_PointOnHatching) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : HatchGen_PointsOnHatching) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> HatchGen_PointOnHatching: 
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
    def Prepend(self,theSeq : HatchGen_PointsOnHatching) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : HatchGen_PointOnHatching) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : HatchGen_PointOnHatching) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : HatchGen_PointsOnHatching) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> HatchGen_PointOnHatching: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : HatchGen_PointsOnHatching) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
HatchGen_IncoherentParity: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_IncoherentParity: 3>
HatchGen_IncompatibleStates: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_IncompatibleStates: 4>
HatchGen_NoProblem: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_NoProblem: 0>
HatchGen_TANGENT: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TANGENT: 2>
HatchGen_TOUCH: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TOUCH: 1>
HatchGen_TRUE: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_TRUE: 0>
HatchGen_TransitionFailure: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_TransitionFailure: 2>
HatchGen_TrimFailure: OCP.HatchGen.HatchGen_ErrorStatus # value = <HatchGen_ErrorStatus.HatchGen_TrimFailure: 1>
HatchGen_UNDETERMINED: OCP.HatchGen.HatchGen_IntersectionType # value = <HatchGen_IntersectionType.HatchGen_UNDETERMINED: 3>
