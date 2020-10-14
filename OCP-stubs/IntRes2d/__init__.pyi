import OCP.IntRes2d
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.NCollection
import OCP.gp
__all__  = [
"IntRes2d_Domain",
"IntRes2d_Intersection",
"IntRes2d_IntersectionPoint",
"IntRes2d_IntersectionSegment",
"IntRes2d_Position",
"IntRes2d_SequenceOfIntersectionPoint",
"IntRes2d_SequenceOfIntersectionSegment",
"IntRes2d_Situation",
"IntRes2d_Transition",
"IntRes2d_TypeTrans",
"IntRes2d_End",
"IntRes2d_Head",
"IntRes2d_In",
"IntRes2d_Inside",
"IntRes2d_Middle",
"IntRes2d_Out",
"IntRes2d_Outside",
"IntRes2d_Touch",
"IntRes2d_Undecided",
"IntRes2d_Unknown"
]
class IntRes2d_Domain():
    """
    Definition of the domain of parameter on a 2d-curve. Most of the time, a domain is defined by two extremities. An extremity is made of : - a point in 2d-space (Pnt2d from gp), - a parameter on the curve, - a tolerance in the 2d-space. Sometimes, it can be made of 0 or 1 point ( for an infinite or semi-infinite line for example).
    """
    def EquivalentParameters(self) -> Tuple[float, float]: 
        """
        Returns Equivalent parameters if the domain is closed. Otherwise, the exception DomainError is raised.

        Returns Equivalent parameters if the domain is closed. Otherwise, the exception DomainError is raised.
        """
    def FirstParameter(self) -> float: 
        """
        Returns the parameter of the first point of the domain The exception DomainError is raised if HasFirstPoint returns False.

        Returns the parameter of the first point of the domain The exception DomainError is raised if HasFirstPoint returns False.
        """
    def FirstPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the first point of the domain. The exception DomainError is raised if HasFirstPoint returns False.

        Returns the first point of the domain. The exception DomainError is raised if HasFirstPoint returns False.
        """
    def FirstTolerance(self) -> float: 
        """
        Returns the tolerance of the first (left) bound. The exception DomainError is raised if HasFirstPoint returns False.

        Returns the tolerance of the first (left) bound. The exception DomainError is raised if HasFirstPoint returns False.
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the domain has a first point, i-e a point defining the lowest admitted parameter on the curve.

        Returns True if the domain has a first point, i-e a point defining the lowest admitted parameter on the curve.
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the domain has a last point, i-e a point defining the highest admitted parameter on the curve.

        Returns True if the domain has a last point, i-e a point defining the highest admitted parameter on the curve.
        """
    def IsClosed(self) -> bool: 
        """
        Returns True if the domain is closed.

        Returns True if the domain is closed.
        """
    def LastParameter(self) -> float: 
        """
        Returns the parameter of the last point of the domain. The exception DomainError is raised if HasLastPoint returns False.

        Returns the parameter of the last point of the domain. The exception DomainError is raised if HasLastPoint returns False.
        """
    def LastPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the last point of the domain. The exception DomainError is raised if HasLastPoint returns False.

        Returns the last point of the domain. The exception DomainError is raised if HasLastPoint returns False.
        """
    def LastTolerance(self) -> float: 
        """
        Returns the tolerance of the last (right) bound. The exception DomainError is raised if HasLastPoint returns False.

        Returns the tolerance of the last (right) bound. The exception DomainError is raised if HasLastPoint returns False.
        """
    @overload
    def SetEquivalentParameters(self,p_first : float,p_last : float) -> None: 
        """
        Defines a closed domain.

        Defines a closed domain.
        """
    @overload
    def SetEquivalentParameters(self,zero : float,period : float) -> None: ...
    @overload
    def SetValues(self) -> None: 
        """
        Sets the values for a bounded domain.

        Sets the values for an infinite domain.

        Sets the values for a semi-infinite domain.
        """
    @overload
    def SetValues(self,Pnt1 : OCP.gp.gp_Pnt2d,Par1 : float,Tol1 : float,Pnt2 : OCP.gp.gp_Pnt2d,Par2 : float,Tol2 : float) -> None: ...
    @overload
    def SetValues(self,Pnt : OCP.gp.gp_Pnt2d,Par : float,Tol : float,First : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Pnt : OCP.gp.gp_Pnt2d,Par : float,Tol : float,First : bool) -> None: ...
    @overload
    def __init__(self,Pnt1 : OCP.gp.gp_Pnt2d,Par1 : float,Tol1 : float,Pnt2 : OCP.gp.gp_Pnt2d,Par2 : float,Tol2 : float) -> None: ...
    pass
class IntRes2d_Intersection():
    """
    Defines the root class of all the Intersections between two 2D-Curves, and provides all the methods about the results of the Intersections Algorithms.
    """
    def IsDone(self) -> bool: 
        """
        returns TRUE when the computation was successful.

        returns TRUE when the computation was successful.
        """
    def IsEmpty(self) -> bool: 
        """
        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.

        Returns TRUE if there is no intersection between the given arguments. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbPoints(self) -> int: 
        """
        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection points between the 2 curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def NbSegments(self) -> int: 
        """
        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.

        This function returns the number of intersection segments between the two curves. The exception NotDone is raised if IsDone returns FALSE.
        """
    def Point(self,N : int) -> IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: ...
    pass
class IntRes2d_IntersectionPoint():
    """
    Definition of an intersection point between two 2D curves.
    """
    def ParamOnFirst(self) -> float: 
        """
        Returns the parameter on the first curve.

        Returns the parameter on the first curve.
        """
    def ParamOnSecond(self) -> float: 
        """
        Returns the parameter on the second curve.

        Returns the parameter on the second curve.
        """
    def SetValues(self,P : OCP.gp.gp_Pnt2d,Uc1 : float,Uc2 : float,Trans1 : IntRes2d_Transition,Trans2 : IntRes2d_Transition,ReversedFlag : bool) -> None: 
        """
        Sets the values for an existing intersection point. The meaning of the parameters are the same as for the Create.

        Sets the values for an existing intersection point. The meaning of the parameters are the same as for the Create.
        """
    def TransitionOfFirst(self) -> IntRes2d_Transition: 
        """
        Returns the transition of the 1st curve compared to the 2nd one.

        Returns the transition of the 1st curve compared to the 2nd one.
        """
    def TransitionOfSecond(self) -> IntRes2d_Transition: 
        """
        returns the transition of the 2nd curve compared to the 1st one.

        returns the transition of the 2nd curve compared to the 1st one.
        """
    def Value(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns the value of the coordinates of the intersection point in the 2D space.

        Returns the value of the coordinates of the intersection point in the 2D space.
        """
    @overload
    def __init__(self,P : OCP.gp.gp_Pnt2d,Uc1 : float,Uc2 : float,Trans1 : IntRes2d_Transition,Trans2 : IntRes2d_Transition,ReversedFlag : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class IntRes2d_IntersectionSegment():
    """
    Definition of an intersection curve between two 2D curves.
    """
    def FirstPoint(self) -> IntRes2d_IntersectionPoint: 
        """
        Returns the first point of the segment as an IntersectionPoint (with a transition). The exception DomainError is raised if HasFirstPoint returns False.

        Returns the first point of the segment as an IntersectionPoint (with a transition). The exception DomainError is raised if HasFirstPoint returns False.
        """
    def HasFirstPoint(self) -> bool: 
        """
        Returns True if the segment is limited by a first point. This point defines the lowest parameter admitted on the first curve for the segment. If IsOpposite returns False, it defines the lowest parameter on the second curve, otherwise, it is the highest parameter on the second curve.

        Returns True if the segment is limited by a first point. This point defines the lowest parameter admitted on the first curve for the segment. If IsOpposite returns False, it defines the lowest parameter on the second curve, otherwise, it is the highest parameter on the second curve.
        """
    def HasLastPoint(self) -> bool: 
        """
        Returns True if the segment is limited by a last point. This point defines the highest parameter admitted on the first curve for the segment. If IsOpposite returns False, it defines the highest parameter on the second curve, otherwise, it is the lowest parameter on the second curve.

        Returns True if the segment is limited by a last point. This point defines the highest parameter admitted on the first curve for the segment. If IsOpposite returns False, it defines the highest parameter on the second curve, otherwise, it is the lowest parameter on the second curve.
        """
    def IsOpposite(self) -> bool: 
        """
        Returns FALSE if the intersection segment has got the same orientation on both curves.

        Returns FALSE if the intersection segment has got the same orientation on both curves.
        """
    def LastPoint(self) -> IntRes2d_IntersectionPoint: 
        """
        Returns the last point of the segment as an IntersectionPoint (with a transition). The exception DomainError is raised if HasLastExtremity returns False.

        Returns the last point of the segment as an IntersectionPoint (with a transition). The exception DomainError is raised if HasLastExtremity returns False.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,P : IntRes2d_IntersectionPoint,First : bool,Oppos : bool,ReverseFlag : bool) -> None: ...
    @overload
    def __init__(self,Oppos : bool) -> None: ...
    @overload
    def __init__(self,P1 : IntRes2d_IntersectionPoint,P2 : IntRes2d_IntersectionPoint,Oppos : bool,ReverseFlag : bool) -> None: ...
    pass
class IntRes2d_Position():
    """
    None

    Members:

      IntRes2d_Head

      IntRes2d_Middle

      IntRes2d_End
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
    IntRes2d_End: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_End
    IntRes2d_Head: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_Head
    IntRes2d_Middle: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_Middle
    __entries: dict # value = {'IntRes2d_Head': (IntRes2d_Position.IntRes2d_Head, None), 'IntRes2d_Middle': (IntRes2d_Position.IntRes2d_Middle, None), 'IntRes2d_End': (IntRes2d_Position.IntRes2d_End, None)}
    __members__: dict # value = {'IntRes2d_Head': IntRes2d_Position.IntRes2d_Head, 'IntRes2d_Middle': IntRes2d_Position.IntRes2d_Middle, 'IntRes2d_End': IntRes2d_Position.IntRes2d_End}
    pass
class IntRes2d_SequenceOfIntersectionPoint(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theSeq : IntRes2d_SequenceOfIntersectionPoint) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theItem : IntRes2d_IntersectionPoint) -> None: ...
    def Assign(self,theOther : IntRes2d_SequenceOfIntersectionPoint) -> IntRes2d_SequenceOfIntersectionPoint: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntRes2d_IntersectionPoint: 
        """
        First item access
        """
    def ChangeLast(self) -> IntRes2d_IntersectionPoint: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntRes2d_IntersectionPoint: 
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
    def First(self) -> IntRes2d_IntersectionPoint: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntRes2d_IntersectionPoint) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionPoint) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionPoint) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntRes2d_IntersectionPoint) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntRes2d_IntersectionPoint: 
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
    def Prepend(self,theSeq : IntRes2d_SequenceOfIntersectionPoint) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theItem : IntRes2d_IntersectionPoint) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntRes2d_IntersectionPoint) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionPoint) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntRes2d_IntersectionPoint: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self,theOther : IntRes2d_SequenceOfIntersectionPoint) -> None: ...
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
class IntRes2d_SequenceOfIntersectionSegment(OCP.NCollection.NCollection_BaseSequence):
    """
    Purpose: Definition of a sequence of elements indexed by an Integer in range of 1..n
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    @overload
    def Append(self,theItem : IntRes2d_IntersectionSegment) -> None: 
        """
        Append one item

        Append another sequence (making it empty)
        """
    @overload
    def Append(self,theSeq : IntRes2d_SequenceOfIntersectionSegment) -> None: ...
    def Assign(self,theOther : IntRes2d_SequenceOfIntersectionSegment) -> IntRes2d_SequenceOfIntersectionSegment: 
        """
        Replace this sequence by the items of theOther. This method does not change the internal allocator.
        """
    def ChangeFirst(self) -> IntRes2d_IntersectionSegment: 
        """
        First item access
        """
    def ChangeLast(self) -> IntRes2d_IntersectionSegment: 
        """
        Last item access
        """
    def ChangeValue(self,theIndex : int) -> IntRes2d_IntersectionSegment: 
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
    def First(self) -> IntRes2d_IntersectionSegment: 
        """
        First item access
        """
    @overload
    def InsertAfter(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionSegment) -> None: 
        """
        InsertAfter theIndex another sequence (making it empty)

        InsertAfter theIndex theItem
        """
    @overload
    def InsertAfter(self,theIndex : int,theItem : IntRes2d_IntersectionSegment) -> None: ...
    @overload
    def InsertBefore(self,theIndex : int,theItem : IntRes2d_IntersectionSegment) -> None: 
        """
        InsertBefore theIndex theItem

        InsertBefore theIndex another sequence (making it empty)
        """
    @overload
    def InsertBefore(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionSegment) -> None: ...
    def IsEmpty(self) -> bool: 
        """
        Empty query
        """
    def Last(self) -> IntRes2d_IntersectionSegment: 
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
    def Prepend(self,theItem : IntRes2d_IntersectionSegment) -> None: 
        """
        Prepend one item

        Prepend another sequence (making it empty)
        """
    @overload
    def Prepend(self,theSeq : IntRes2d_SequenceOfIntersectionSegment) -> None: ...
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
    def SetValue(self,theIndex : int,theItem : IntRes2d_IntersectionSegment) -> None: 
        """
        Set item value by theIndex
        """
    def Size(self) -> int: 
        """
        Number of items
        """
    def Split(self,theIndex : int,theSeq : IntRes2d_SequenceOfIntersectionSegment) -> None: 
        """
        Split in two sequences
        """
    def Upper(self) -> int: 
        """
        Method for consistency with other collections.
        """
    def Value(self,theIndex : int) -> IntRes2d_IntersectionSegment: 
        """
        Constant item access by theIndex
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theOther : IntRes2d_SequenceOfIntersectionSegment) -> None: ...
    @overload
    def __init__(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: ...
    def __iter__(self) -> iterator: ...
    @staticmethod
    def delNode_s(theNode : NCollection_SeqNode,theAl : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Static deleter to be passed to BaseSequence
        """
    pass
class IntRes2d_Situation():
    """
    None

    Members:

      IntRes2d_Inside

      IntRes2d_Outside

      IntRes2d_Unknown
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
    IntRes2d_Inside: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Inside
    IntRes2d_Outside: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Outside
    IntRes2d_Unknown: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Unknown
    __entries: dict # value = {'IntRes2d_Inside': (IntRes2d_Situation.IntRes2d_Inside, None), 'IntRes2d_Outside': (IntRes2d_Situation.IntRes2d_Outside, None), 'IntRes2d_Unknown': (IntRes2d_Situation.IntRes2d_Unknown, None)}
    __members__: dict # value = {'IntRes2d_Inside': IntRes2d_Situation.IntRes2d_Inside, 'IntRes2d_Outside': IntRes2d_Situation.IntRes2d_Outside, 'IntRes2d_Unknown': IntRes2d_Situation.IntRes2d_Unknown}
    pass
class IntRes2d_Transition():
    """
    Definition of the type of transition near an intersection point between two curves. The transition is either a "true transition", which means that one of the curves goes inside or outside the area defined by the other curve near the intersection, or a "touch transition" which means that the first curve does not cross the other one, or an "undecided" transition, which means that the curves are superposed.
    """
    def IsOpposite(self) -> bool: 
        """
        returns a significant value if TransitionType returns TOUCH. In this case, the function returns true when the 2 curves locally define two different parts of the space. If TransitionType returns IN or OUT or UNDECIDED, the exception DomainError is raised.

        returns a significant value if TransitionType returns TOUCH. In this case, the function returns true when the 2 curves locally define two different parts of the space. If TransitionType returns IN or OUT or UNDECIDED, the exception DomainError is raised.
        """
    def IsTangent(self) -> bool: 
        """
        Returns TRUE when the 2 curves are tangent at the intersection point. Theexception DomainError is raised if the type of transition is UNDECIDED.

        Returns TRUE when the 2 curves are tangent at the intersection point. Theexception DomainError is raised if the type of transition is UNDECIDED.
        """
    def PositionOnCurve(self) -> IntRes2d_Position: 
        """
        Indicates if the intersection is at the beginning (IntRes2d_Head), at the end (IntRes2d_End), or in the middle (IntRes2d_Middle) of the curve.

        Indicates if the intersection is at the beginning (IntRes2d_Head), at the end (IntRes2d_End), or in the middle (IntRes2d_Middle) of the curve.
        """
    def SetPosition(self,Pos : IntRes2d_Position) -> None: 
        """
        Sets the value of the position.

        Sets the value of the position.
        """
    @overload
    def SetValue(self,Pos : IntRes2d_Position) -> None: 
        """
        Sets the values of an IN or OUT transition.

        Sets the values of a TOUCH transition.

        Sets the values of an UNDECIDED transition.

        Sets the values of an IN or OUT transition.

        Sets the values of a TOUCH transition.

        Sets the values of an UNDECIDED transition.
        """
    @overload
    def SetValue(self,Tangent : bool,Pos : IntRes2d_Position,Type : IntRes2d_TypeTrans) -> None: ...
    @overload
    def SetValue(self,Tangent : bool,Pos : IntRes2d_Position,Situ : IntRes2d_Situation,Oppos : bool) -> None: ...
    def Situation(self) -> IntRes2d_Situation: 
        """
        returns a significant value if TransitionType returns TOUCH. In this case, the function returns : INSIDE when the curve remains inside the other one, OUTSIDE when it remains outside the other one, UNKNOWN when the calculus, based on the second derivatives cannot give the result. If TransitionType returns IN or OUT or UNDECIDED, the exception DomainError is raised.

        returns a significant value if TransitionType returns TOUCH. In this case, the function returns : INSIDE when the curve remains inside the other one, OUTSIDE when it remains outside the other one, UNKNOWN when the calculus, based on the second derivatives cannot give the result. If TransitionType returns IN or OUT or UNDECIDED, the exception DomainError is raised.
        """
    def TransitionType(self) -> IntRes2d_TypeTrans: 
        """
        Returns the type of transition at the intersection. It may be IN or OUT or TOUCH, or UNDECIDED if the two first derivatives are not enough to give the tangent to one of the two curves.

        Returns the type of transition at the intersection. It may be IN or OUT or TOUCH, or UNDECIDED if the two first derivatives are not enough to give the tangent to one of the two curves.
        """
    @overload
    def __init__(self,Tangent : bool,Pos : IntRes2d_Position,Type : IntRes2d_TypeTrans) -> None: ...
    @overload
    def __init__(self,Tangent : bool,Pos : IntRes2d_Position,Situ : IntRes2d_Situation,Oppos : bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Pos : IntRes2d_Position) -> None: ...
    pass
class IntRes2d_TypeTrans():
    """
    None

    Members:

      IntRes2d_In

      IntRes2d_Out

      IntRes2d_Touch

      IntRes2d_Undecided
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
    IntRes2d_In: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_In
    IntRes2d_Out: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Out
    IntRes2d_Touch: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Touch
    IntRes2d_Undecided: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Undecided
    __entries: dict # value = {'IntRes2d_In': (IntRes2d_TypeTrans.IntRes2d_In, None), 'IntRes2d_Out': (IntRes2d_TypeTrans.IntRes2d_Out, None), 'IntRes2d_Touch': (IntRes2d_TypeTrans.IntRes2d_Touch, None), 'IntRes2d_Undecided': (IntRes2d_TypeTrans.IntRes2d_Undecided, None)}
    __members__: dict # value = {'IntRes2d_In': IntRes2d_TypeTrans.IntRes2d_In, 'IntRes2d_Out': IntRes2d_TypeTrans.IntRes2d_Out, 'IntRes2d_Touch': IntRes2d_TypeTrans.IntRes2d_Touch, 'IntRes2d_Undecided': IntRes2d_TypeTrans.IntRes2d_Undecided}
    pass
IntRes2d_End: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_End
IntRes2d_Head: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_Head
IntRes2d_In: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_In
IntRes2d_Inside: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Inside
IntRes2d_Middle: OCP.IntRes2d.IntRes2d_Position # value = IntRes2d_Position.IntRes2d_Middle
IntRes2d_Out: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Out
IntRes2d_Outside: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Outside
IntRes2d_Touch: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Touch
IntRes2d_Undecided: OCP.IntRes2d.IntRes2d_TypeTrans # value = IntRes2d_TypeTrans.IntRes2d_Undecided
IntRes2d_Unknown: OCP.IntRes2d.IntRes2d_Situation # value = IntRes2d_Situation.IntRes2d_Unknown
