import OCP.BRepClass
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
from numpy import float64
_Shape = Tuple[int, ...]
import OCP.TopAbs
import OCP.IntRes2d
import OCP.TopoDS
import OCP.Geom2dInt
import OCP.gp
__all__  = [
"BRepClass_Edge",
"BRepClass_FClass2dOfFClassifier",
"BRepClass_FClassifier",
"BRepClass_FaceClassifier",
"BRepClass_FaceExplorer",
"BRepClass_FacePassiveClassifier",
"BRepClass_Intersector"
]
class BRepClass_Edge():
    """
    This class is used to send the description of an Edge to the classifier. It contains an Edge and a Face. So the PCurve of the Edge can be found.
    """
    def Edge(self) -> OCP.TopoDS.TopoDS_Edge: 
        """
        None

        None

        None

        None
        """
    def Face(self) -> OCP.TopoDS.TopoDS_Face: 
        """
        None

        None

        None

        None
        """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self,E : OCP.TopoDS.TopoDS_Edge,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepClass_FClass2dOfFClassifier():
    """
    None
    """
    def ClosestIntersection(self) -> int: 
        """
        Returns 0 if the last compared edge had no relevant intersection. Else returns the index of this intersection in the last intersection algorithm.
        """
    def Compare(self,E : BRepClass_Edge,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the classification process with the edge <E> from the boundary.
        """
    def Intersector(self) -> BRepClass_Intersector: 
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
class BRepClass_FClassifier():
    """
    None
    """
    def Edge(self) -> BRepClass_Edge: 
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
    def Perform(self,F : BRepClass_FaceExplorer,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: 
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
    def __init__(self,F : BRepClass_FaceExplorer,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: ...
    pass
class BRepClass_FaceClassifier(BRepClass_FClassifier):
    """
    Provides Constructors with a Face.
    """
    def Edge(self) -> BRepClass_Edge: 
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
    @overload
    def Perform(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt,Tol : float) -> None: 
        """
        Classify the Point P with Tolerance <T> on the face described by <F>.

        Classify the Point P with Tolerance <T> on the face described by <F>.
        """
    @overload
    def Perform(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: ...
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
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: ...
    @overload
    def __init__(self,F : BRepClass_FaceExplorer,P : OCP.gp.gp_Pnt2d,Tol : float) -> None: ...
    @overload
    def __init__(self,F : OCP.TopoDS.TopoDS_Face,P : OCP.gp.gp_Pnt,Tol : float) -> None: ...
    @overload
    def __init__(self) -> None: ...
    pass
class BRepClass_FaceExplorer():
    """
    Provide an exploration of a BRep Face for the classification. Return UV edges.
    """
    def CheckPoint(self,thePoint : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Checks the point and change its coords if it is located too far from the bounding box of the face. New Coordinates of the point will be on the line between the point and the center of the bounding box. Returns True if point was not changed.
        """
    def CurrentEdge(self,E : BRepClass_Edge,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Current edge in current wire and its orientation.
        """
    def InitEdges(self) -> None: 
        """
        Starts an exploration of the edges of the current wire.
        """
    def InitWires(self) -> None: 
        """
        Starts an exploration of the wires.
        """
    def MoreEdges(self) -> bool: 
        """
        Returns True if there is a current edge.

        Returns True if there is a current edge.
        """
    def MoreWires(self) -> bool: 
        """
        Returns True if there is a current wire.

        Returns True if there is a current wire.
        """
    def NextEdge(self) -> None: 
        """
        Sets the explorer to the next edge.

        Sets the explorer to the next edge.
        """
    def NextWire(self) -> None: 
        """
        Sets the explorer to the next wire.

        Sets the explorer to the next wire.
        """
    def OtherSegment(self,P : OCP.gp.gp_Pnt2d,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        Returns in <L>, <Par> a segment having at least one intersection with the face boundary to compute intersections. Each call gives another segment.
        """
    def Reject(self,P : OCP.gp.gp_Pnt2d) -> bool: 
        """
        Should return True if the point is outside a bounding volume of the face.
        """
    def RejectEdge(self,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        Returns True if the edge bounding volume does not intersect the segment.
        """
    def RejectWire(self,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        Returns True if the wire bounding volume does not intersect the segment.
        """
    def Segment(self,P : OCP.gp.gp_Pnt2d,L : OCP.gp.gp_Lin2d,Par : float) -> bool: 
        """
        Returns in <L>, <Par> a segment having at least one intersection with the face boundary to compute intersections.
        """
    def __init__(self,F : OCP.TopoDS.TopoDS_Face) -> None: ...
    pass
class BRepClass_FacePassiveClassifier():
    """
    None
    """
    def ClosestIntersection(self) -> int: 
        """
        Returns 0 if the last compared edge had no relevant intersection. Else returns the index of this intersection in the last intersection algorithm.
        """
    def Compare(self,E : BRepClass_Edge,Or : OCP.TopAbs.TopAbs_Orientation) -> None: 
        """
        Updates the classification process with the edge <E> from the boundary.
        """
    def Intersector(self) -> BRepClass_Intersector: 
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
class BRepClass_Intersector(OCP.Geom2dInt.Geom2dInt_IntConicCurveOfGInter, OCP.IntRes2d.IntRes2d_Intersection):
    """
    Intersect an Edge with a segment. Implement the Intersector2d required by the classifier.
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
    def LocalGeometry(self,E : BRepClass_Edge,U : float,T : OCP.gp.gp_Dir2d,N : OCP.gp.gp_Dir2d) -> Tuple[float]: 
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
    def Perform(self,L : OCP.gp.gp_Lin2d,P : float,Tol : float,E : BRepClass_Edge) -> None: 
        """
        Intersect the line segment and the edge.
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
    @overload
    def SetReversedParameters(self,Reverseflag : bool) -> None: 
        """
        None

        None
        """
    @overload
    def SetReversedParameters(self,flag : bool) -> None: ...
    def __init__(self) -> None: ...
    pass
