import OCP.Geom2dHatch
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.HatchGen
import OCP.Geom2dAdaptor
import OCP.Adaptor2d
import OCP.NCollection
import io
import OCP.gp
import OCP.Geom2d
import OCP.TopAbs
import OCP.IntRes2d
import OCP.Geom2dInt
__all__  = [
"Geom2dHatch_Classifier",
"Geom2dHatch_Element",
"Geom2dHatch_Elements",
"Geom2dHatch_FClass2dOfClassifier",
"Geom2dHatch_Hatcher",
"Geom2dHatch_Hatching",
"Geom2dHatch_Intersector",
"Geom2dHatch_MapOfElements"
]
class Geom2dHatch_Classifier():
    """
    None
    """
    def Edge(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the Edge used to determine the classification. When the State is ON this is the Edge containing the point.
        """
    def EdgeParameter(self) -> float: 
        """
        Returns the parameter on Edge() used to determine the classification.
        """
    def NoWires(self) -> bool: 
        """
        Returns True if the face contains no wire. The state is IN.
        """
    def Perform(self,F : Geom2dHatch_Elements,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: 
        """
        Classify the Point P with Tolerance <T> on the face described by <F>.
        """
    def Position(self) -> OCP.IntRes2d.IntRes2d_Position: 
        """
        Returns the position of the point on the edge returned by Edge.
        """
    def Rejected(self) -> bool: 
        """
        Returns True when the state was computed by a rejection. The state is OUT.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the result of the classification.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,F : Geom2dHatch_Elements,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: ...
    pass
class Geom2dHatch_Element():
    """
    None
    """
    def ChangeCurve(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the element.
        """
    def Curve(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the element.
        """
    @overload
    def Orientation(self,Orientation : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Sets the orientation of the element.

        Returns the orientation of the element.
        """
    @overload
    def Orientation(self) -> OCP.TopAbs.TopAbs_Orientation: ...
    @overload
    def __init__(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Orientation : OCP.TopAbs.TopAbs_Orientation=TopAbs_Orientation.TopAbs_FORWARD) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dHatch_Elements():
    """
    None
    """
    def Bind(self,K : int,I : Geom2dHatch_Element) -> bool: 
        """
        None
        """
    def ChangeFind(self,K : int) -> Geom2dHatch_Element: 
        """
        None
        """
    def CheckPoint(self,P : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None
        """
    def Clear(self) -> None: 
        """
        None
        """
    def CurrentEdge(self,E : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        None
        """
    def Find(self,K : int) -> Geom2dHatch_Element: 
        """
        None
        """
    def InitEdges(self) -> None: 
        """
        None
        """
    def InitWires(self) -> None: 
        """
        None
        """
    def IsBound(self,K : int) -> bool: 
        """
        None
        """
    def MoreEdges(self) -> bool: 
        """
        None
        """
    def MoreWires(self) -> bool: 
        """
        None
        """
    def NextEdge(self) -> None: 
        """
        None
        """
    def NextWire(self) -> None: 
        """
        None
        """
    def OtherSegment(self,P : OCP.gp.gp_Pnt2d,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        None
        """
    def Reject(self,P : OCP.gp.gp_Pnt2d) -> bool: 
        """
        None
        """
    def RejectEdge(self,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        None
        """
    def RejectWire(self,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        None
        """
    def Segment(self,P : OCP.gp.gp_Pnt2d,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        None
        """
    def UnBind(self,K : int) -> bool: 
        """
        None
        """
    @overload
    def __init__(self,Other : Geom2dHatch_Elements) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class Geom2dHatch_FClass2dOfClassifier():
    """
    None
    """
    def ClosestIntersection(self) -> int: 
        """
        Returns 0 if the last compared edge had no relevant intersection. Else returns the index of this intersection in the last intersection algorithm.
        """
    def Compare(self,E : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the classification process with the edge <E> from the boundary.
        """
    def Intersector(self) -> Geom2dHatch_Intersector: 
        """
        Returns the intersecting algorithm.
        """
    def IsHeadOrEnd(self) -> bool: 
        """
        Returns the Standard_True if the closest intersection point represents head or end of the edge. Returns Standard_False otherwise.
        """
    def Parameter(self) -> float: 
        """
        Returns the current value of the parameter.
        """
    def Reset(self,L : OCP.gp.gp_Lin2d,P : float,Tol : float) -> None: 
        """
        Starts a classification process. The point to classify is the origin of the line <L>. <P> is the original length of the segment on <L> used to compute intersections. <Tol> is the tolerance attached to the line segment in intersections.
        """
    def State(self) -> OCP.TopAbs.TopAbs_State: 
        """
        Returns the current state of the point.
        """
    def __init__(self) -> None: ...
    pass
class Geom2dHatch_Hatcher():
    """
    None
    """
    @overload
    def AddElement(self,Curve : OCP.Geom2d.Geom2d_Curve,Orientation : OCP.TopAbs.TopAbs_Orientation=TopAbs_Orientation.TopAbs_FORWARD) -> int: 
        """
        Adds an element to the hatcher and returns its index.

        Adds an element to the hatcher and returns its index.
        """
    @overload
    def AddElement(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,Orientation : OCP.TopAbs.TopAbs_Orientation=TopAbs_Orientation.TopAbs_FORWARD) -> int: ...
    def AddHatching(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int: 
        """
        Adds a hatching to the hatcher and returns its index.
        """
    def ChangeIntersector(self) -> Geom2dHatch_Intersector: 
        """
        Returns the associated intersector.

        Returns the associated intersector.
        """
    def Clear(self) -> None: 
        """
        Removes all the hatchings and all the elements.

        Removes all the hatchings and all the elements.
        """
    def ClrElements(self) -> None: 
        """
        Removes all the elements from the hatcher.
        """
    def ClrHatchings(self) -> None: 
        """
        Removes all the hatchings from the hatcher.
        """
    @overload
    def ComputeDomains(self,IndH : int) -> None: 
        """
        Computes the domains of all the hatchings.

        Computes the domains of the IndH-th hatching.
        """
    @overload
    def ComputeDomains(self) -> None: ...
    @overload
    def Confusion2d(self) -> float: 
        """
        Sets the confusion tolerance.

        Returns the 2d confusion tolerance, i.e. the value under which two points are considered identical in the parametric space of the hatching.

        Returns the 2d confusion tolerance, i.e. the value under which two points are considered identical in the parametric space of the hatching.
        """
    @overload
    def Confusion2d(self,Confusion : float) -> None: ...
    @overload
    def Confusion3d(self,Confusion : float) -> None: 
        """
        Sets the confusion tolerance.

        Returns the 3d confusion tolerance, i.e. the value under which two points are considered identical in the 3d space of the hatching.

        Returns the 3d confusion tolerance, i.e. the value under which two points are considered identical in the 3d space of the hatching.
        """
    @overload
    def Confusion3d(self) -> float: ...
    def Domain(self,IndH : int,IDom : int) -> OCP.HatchGen.HatchGen_Domain: 
        """
        Returns the IDom-th domain of the IndH-th hatching.
        """
    def Dump(self) -> None: 
        """
        Dump the hatcher.
        """
    def ElementCurve(self,IndE : int) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the IndE-th element.

        Returns the curve associated to the IndE-th element.
        """
    def HatchingCurve(self,IndH : int) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the IndH-th hatching.

        Returns the curve associated to the IndH-th hatching.
        """
    @overload
    def Intersector(self) -> Geom2dHatch_Intersector: 
        """
        Sets the associated intersector.

        Returns the associated intersector.

        Returns the associated intersector.
        """
    @overload
    def Intersector(self,Intersector : Geom2dHatch_Intersector) -> None: ...
    def IsDone(self,IndH : int) -> bool: 
        """
        Returns the fact that the domains were computed for the IndH-th hatching.

        Returns the fact that the domains were computed for the IndH-th hatching.
        """
    @overload
    def KeepPoints(self,Keep : bool) -> None: 
        """
        Sets the above flag.

        Returns the flag about the points consideration.

        Returns the flag about the points consideration.
        """
    @overload
    def KeepPoints(self) -> bool: ...
    @overload
    def KeepSegments(self,Keep : bool) -> None: 
        """
        Sets the above flag.

        Returns the flag about the segments consideration.

        Returns the flag about the segments consideration.
        """
    @overload
    def KeepSegments(self) -> bool: ...
    def NbDomains(self,IndH : int) -> int: 
        """
        Returns the number of domains of the IndH-th hatching. Only ONE "INFINITE" domain means that the hatching is fully included in the contour defined by the elements.

        Returns the number of domains of the IndH-th hatching. Only ONE "INFINITE" domain means that the hatching is fully included in the contour defined by the elements.
        """
    def NbPoints(self,IndH : int) -> int: 
        """
        Returns the number of intersection points of the IndH-th hatching.

        Returns the number of intersection points of the IndH-th hatching.
        """
    def Point(self,IndH : int,IndP : int) -> OCP.HatchGen.HatchGen_PointOnHatching: 
        """
        Returns the IndP-th intersection point of the IndH-th hatching.

        Returns the IndP-th intersection point of the IndH-th hatching.
        """
    def RemElement(self,IndE : int) -> None: 
        """
        Removes the IndE-th element from the hatcher.
        """
    def RemHatching(self,IndH : int) -> None: 
        """
        Removes the IndH-th hatching from the hatcher.
        """
    def Status(self,IndH : int) -> OCP.HatchGen.HatchGen_ErrorStatus: 
        """
        Returns the status about the IndH-th hatching.

        Returns the status about the IndH-th hatching.
        """
    @overload
    def Trim(self,IndH : int) -> None: 
        """
        Trims all the hatchings of the hatcher by all the elements of the hatcher.

        Adds a hatching to the hatcher and trims it by the elements already given and returns its index.

        Trims the IndH-th hatching by the elements already given.
        """
    @overload
    def Trim(self) -> None: ...
    @overload
    def Trim(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> int: ...
    def TrimDone(self,IndH : int) -> bool: 
        """
        Returns the fact that the intersections were computed for the IndH-th hatching.

        Returns the fact that the intersections were computed for the IndH-th hatching.
        """
    def TrimFailed(self,IndH : int) -> bool: 
        """
        Returns the fact that the intersections failed for the IndH-th hatching.

        Returns the fact that the intersections failed for the IndH-th hatching.
        """
    def __init__(self,Intersector : Geom2dHatch_Intersector,Confusion2d : float,Confusion3d : float,KeepPnt : bool=False,KeepSeg : bool=False) -> None: ...
    pass
class Geom2dHatch_Hatching():
    """
    None
    """
    def AddDomain(self,Domain : OCP.HatchGen.HatchGen_Domain) -> None: 
        """
        Adds a domain to the hatching.
        """
    def AddPoint(self,Point : OCP.HatchGen.HatchGen_PointOnHatching,Confusion : float) -> None: 
        """
        Adds an intersection point to the hatching.
        """
    def ChangeCurve(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the hatching.
        """
    def ChangePoint(self,Index : int) -> OCP.HatchGen.HatchGen_PointOnHatching: 
        """
        Returns the Index-th intersection point of the hatching. The exception OutOfRange is raised if Index < 1 or Index > NbPoints.
        """
    def ClassificationPoint(self) -> OCP.gp.gp_Pnt2d: 
        """
        Returns a point on the curve. This point will be used for the classification.
        """
    def ClrDomains(self) -> None: 
        """
        Removes all the domains of the hatching.
        """
    def ClrPoints(self) -> None: 
        """
        Removes all the intersection points of the hatching.
        """
    def Curve(self) -> OCP.Geom2dAdaptor.Geom2dAdaptor_Curve: 
        """
        Returns the curve associated to the hatching.
        """
    def Domain(self,Index : int) -> OCP.HatchGen.HatchGen_Domain: 
        """
        Returns the Index-th domain of the hatching. The exception OutOfRange is raised if Index < 1 or Index > NbDomains.
        """
    @overload
    def IsDone(self) -> bool: 
        """
        Sets the flag about the domains computation to the given value.

        Returns the flag about the domains computation.
        """
    @overload
    def IsDone(self,Flag : bool) -> None: ...
    def NbDomains(self) -> int: 
        """
        Returns the number of domains of the hatching.
        """
    def NbPoints(self) -> int: 
        """
        Returns the number of intersection points of the hatching.
        """
    def Point(self,Index : int) -> OCP.HatchGen.HatchGen_PointOnHatching: 
        """
        Returns the Index-th intersection point of the hatching. The exception OutOfRange is raised if Index < 1 or Index > NbPoints.
        """
    def RemDomain(self,Index : int) -> None: 
        """
        Removes the Index-th domain of the hatching. The exception OutOfRange is raised if Index < 1 or Index > NbDomains.
        """
    def RemPoint(self,Index : int) -> None: 
        """
        Removes the Index-th intersection point of the hatching. The exception OutOfRange is raised if Index < 1 or Index > NbPoints.
        """
    @overload
    def Status(self,theStatus : OCP.HatchGen.HatchGen_ErrorStatus) -> None: 
        """
        Sets the error status.

        Returns the error status.
        """
    @overload
    def Status(self) -> OCP.HatchGen.HatchGen_ErrorStatus: ...
    @overload
    def TrimDone(self) -> bool: 
        """
        Sets the flag about the trimming computations to the given value.

        Returns the flag about the trimming computations.
        """
    @overload
    def TrimDone(self,Flag : bool) -> None: ...
    @overload
    def TrimFailed(self,Flag : bool) -> None: 
        """
        Sets the flag about the trimming failure to the given value.

        Returns the flag about the trimming failure.
        """
    @overload
    def TrimFailed(self) -> bool: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Curve : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: ...
    pass
class Geom2dHatch_Intersector(OCP.Geom2dInt.Geom2dInt_GInter, OCP.IntRes2d.IntRes2d_Intersection):
    """
    None
    """
    def ComputeDomain(self,C1 : OCP.Adaptor2d.Adaptor2d_Curve2d,TolDomain : float) -> OCP.IntRes2d.IntRes2d_Domain: 
        """
        Create a domain from a curve
        """
    def ConfusionTolerance(self) -> float: 
        """
        Returns the confusion tolerance of the intersector.

        Returns the confusion tolerance of the intersector.
        """
    def GetMinNbSamples(self) -> int: 
        """
        None
        """
    def Intersect(self,C1 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,C2 : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: 
        """
        Intersects the curves C1 and C2. The results are retrieved by the usual methods described in IntRes2d_Intersection. Creates an intersector.

        Intersects the curves C1 and C2. The results are retrieved by the usual methods described in IntRes2d_Intersection. Creates an intersector.
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
    def LocalGeometry(self,E : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve,U : float,T : OCP.gp.gp_Dir2d,N : OCP.gp.gp_Dir2d) -> Tuple[float]: 
        """
        Returns in <T>, <N> and <C> the tangent, normal and curvature of the edge <E> at parameter value <U>.
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
    def Perform(self,L : OCP.gp.gp_Lin2d,P : float,Tol : float,E : OCP.Geom2dAdaptor.Geom2dAdaptor_Curve) -> None: 
        """
        Performs the intersection between the 2d line segment (<L>, <P>) and the Curve <E>. The line segment is the part of the 2d line <L> of parameter range [0, <P>] (P is positive and can be RealLast()). Tol is the Tolerance on the segment. The order is relevant, the first argument is the segment, the second the Edge.
        """
    def Point(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionPoint: 
        """
        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection point of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def Segment(self,N : int) -> OCP.IntRes2d.IntRes2d_IntersectionSegment: 
        """
        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).

        This function returns the intersection segment of range N; The exception NotDone is raised if IsDone returns FALSE. The exception OutOfRange is raised if (N <= 0) or (N > NbPoints).
        """
    def SetConfusionTolerance(self,Confusion : float) -> None: 
        """
        Sets the confusion tolerance of the intersector.

        Sets the confusion tolerance of the intersector.
        """
    def SetMinNbSamples(self,theMinNbSamples : int) -> None: 
        """
        Set / get minimum number of points in polygon intersection.
        """
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def SetTangencyTolerance(self,Tangency : float) -> None: 
        """
        Sets the tangency tolerance of the intersector.

        Sets the tangency tolerance of the intersector.
        """
    def TangencyTolerance(self) -> float: 
        """
        Returns the tangency tolerance of the intersector.

        Returns the tangency tolerance of the intersector.
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,Confusion : float,Tangency : float) -> None: ...
    pass
class Geom2dHatch_MapOfElements(OCP.NCollection.NCollection_BaseMap):
    """
    Purpose: The DataMap is a Map to store keys with associated Items. See Map from NCollection for a discussion about the number of buckets.
    """
    def Allocator(self) -> OCP.NCollection.NCollection_BaseAllocator: 
        """
        Returns attached allocator
        """
    def Assign(self,theOther : Geom2dHatch_MapOfElements) -> Geom2dHatch_MapOfElements: 
        """
        Assignment. This method does not change the internal allocator.
        """
    def Bind(self,theKey : int,theItem : Geom2dHatch_Element) -> bool: 
        """
        Bind binds Item to Key in map.
        """
    def Bound(self,theKey : int,theItem : Geom2dHatch_Element) -> Geom2dHatch_Element: 
        """
        Bound binds Item to Key in map. Returns modifiable Item
        """
    def ChangeFind(self,theKey : int) -> Geom2dHatch_Element: 
        """
        ChangeFind returns mofifiable Item by Key. Raises if Key was not bound
        """
    def ChangeSeek(self,theKey : int) -> Geom2dHatch_Element: 
        """
        ChangeSeek returns modifiable pointer to Item by Key. Returns NULL is Key was not bound.
        """
    @overload
    def Clear(self,theAllocator : OCP.NCollection.NCollection_BaseAllocator) -> None: 
        """
        Clear data. If doReleaseMemory is false then the table of buckets is not released and will be reused.

        Clear data and reset allocator
        """
    @overload
    def Clear(self,doReleaseMemory : bool=True) -> None: ...
    def Exchange(self,theOther : Geom2dHatch_MapOfElements) -> None: 
        """
        Exchange the content of two maps without re-allocations. Notice that allocators will be swapped as well!
        """
    def Extent(self) -> int: 
        """
        Extent
        """
    @overload
    def Find(self,theKey : int,theValue : Geom2dHatch_Element) -> bool: 
        """
        Find returns the Item for Key. Raises if Key was not bound

        Find Item for key with copying.
        """
    @overload
    def Find(self,theKey : int) -> Geom2dHatch_Element: ...
    def IsBound(self,theKey : int) -> bool: 
        """
        IsBound
        """
    def IsEmpty(self) -> bool: 
        """
        IsEmpty
        """
    def NbBuckets(self) -> int: 
        """
        NbBuckets
        """
    def ReSize(self,N : int) -> None: 
        """
        ReSize
        """
    def Seek(self,theKey : int) -> Geom2dHatch_Element: 
        """
        Seek returns pointer to Item by Key. Returns NULL is Key was not bound.
        """
    def Size(self) -> int: 
        """
        Size
        """
    def Statistics(self,S : io.BytesIO) -> None: 
        """
        Statistics
        """
    def UnBind(self,theKey : int) -> bool: 
        """
        UnBind removes Item Key pair from map
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,theNbBuckets : int,theAllocator : OCP.NCollection.NCollection_BaseAllocator=None) -> None: ...
    @overload
    def __init__(self,theOther : Geom2dHatch_MapOfElements) -> None: ...
    def __iter__(self) -> Iterator: ...
    pass
